import os

import yaml
from dagster import (
    AssetKey,
    AssetSelection,
    OpExecutionContext,
    asset,
    define_asset_job,
)

with open(
    os.path.join(os.path.dirname(__file__), "..", "configs", "some_config.yaml")
) as f:
    config = yaml.safe_load(f)


@asset(config_schema={"return_value": str})
def my_cool_asset(context: OpExecutionContext):
    return context.op_config["return_value"]


@asset
def my_cooler_asset(my_cool_asset: str):
    return f"{my_cool_asset}!"


my_cool_asset_job = define_asset_job(
    name="my_cool_asset_job",
    selection=AssetSelection.keys(AssetKey("my_cool_asset")).downstream(),
    config=config,
)
