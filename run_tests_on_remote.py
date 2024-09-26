import os

import pytest
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.compute import DataSecurityMode


def get_cluster_id():

    w = WorkspaceClient()
    clusters = list(w.clusters.list())

    testing_cluster_name = "Testing Cluster"
    matched_cluster = [x for x in clusters if x.cluster_name == testing_cluster_name]

    if len(matched_cluster) > 1:
        raise Exception("Duplicate cluster names!")
    elif len(matched_cluster) == 0:
        cluster = w.clusters.create_and_wait(
            cluster_name=testing_cluster_name,
            spark_version="15.4.x-scala2.12",
            spark_conf={
                "spark.master": "local[*, 4]",
            },
            spark_env_vars={"PYSPARK_PYTHON": "/databricks/python3/bin/python3"},
            node_type_id="Standard_D4ds_v5",
            autotermination_minutes=30,
            enable_elastic_disk=True,
            single_user_name=w.current_user.me().user_name,
            num_workers=0,
            data_security_mode=DataSecurityMode.SINGLE_USER,
        )
        cluster_id = cluster.cluster_id
    else:
        cluster_id = matched_cluster[0].cluster_id
        w.clusters.ensure_cluster_is_running(cluster_id=cluster_id)
    return cluster_id


if __name__ == "__main__":
    cluster_id = get_cluster_id()
    os.environ["DATABRICKS_CLUSTER_ID"] = cluster_id
    pytest.main()
