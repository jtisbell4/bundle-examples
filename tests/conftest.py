import os

import dotenv
import pytest


@pytest.fixture(scope="session", autouse=True)
def set_env_vars():
    if os.path.exists(".databricks/.databricks.env"):
        dotenv.load_dotenv(".databricks/.databricks.env")
