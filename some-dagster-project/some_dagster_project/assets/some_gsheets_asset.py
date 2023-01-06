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
    os.path.join(os.path.dirname(__file__), "..", "configs", "some_gsheets_config.yaml")
) as f:
    config = yaml.safe_load(f)


@asset(config_schema={"sheet_mapping": dict}, required_resource_keys={"utils_gsheets"})
def my_gsheets_asset(context: OpExecutionContext):
    return context.resources.utils_gsheets.fetch_sheets_as_csv(context.op_config)


my_gsheets_asset_job = define_asset_job(
    name="my_gsheets_asset_job",
    selection=AssetSelection.keys(AssetKey("my_gsheets_asset")).downstream(),
    config=config,
)
