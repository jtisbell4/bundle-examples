from pyspark.sql import DataFrame, SparkSession


def get_taxis(spark: SparkSession) -> DataFrame:
    return spark.read.table("samples.nyctaxi.trips")


# Create a new Databricks Connect session. If this fails,
# check that you have configured Databricks Connect correctly.
# See https://docs.databricks.com/dev-tools/databricks-connect.html.
# Locally, DATABRICKS_HOST, DATABRICKS_TOKEN, and DATABRICKS_CLUSTER_ID must be set.
# On CI runner, DATABRICKS_HOST, DATABRICKS_CLIENT_ID, DATABRICKS_CLIENT_SECRET, and
# DATABRICKS_CLUSTER_ID must be set.
def get_spark() -> SparkSession:
    from databricks.connect import DatabricksSession

    return DatabricksSession.builder.getOrCreate()


def main():
    get_taxis(get_spark()).show(5)


if __name__ == "__main__":
    main()
