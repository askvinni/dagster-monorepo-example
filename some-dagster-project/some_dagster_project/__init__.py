import os

from dagster import Definitions
from dagster_utils.dagsterhub.sensors import slack_on_run_failure

from .assets.some_asset import *
from .assets.some_gsheets_asset import *
from .resource_defs import *

resources = {
    "prod": RESOURCES_PROD,
    "dev": RESOURCES_DEV,
}

defs = Definitions(
    assets=[
        my_cool_asset,
        my_cooler_asset,
        my_gsheets_asset,
    ],
    jobs=[my_cool_asset_job, my_gsheets_asset_job],
    resources=resources[os.getenv("ENVIRONMENT", "dev")],
    sensors=[slack_on_run_failure],
)
