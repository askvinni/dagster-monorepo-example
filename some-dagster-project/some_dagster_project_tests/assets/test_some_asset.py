from dagster import materialize_to_memory

from some_dagster_project.assets.some_asset import *


def test_cool_assets(asset_configs):
    materialization = materialize_to_memory(
        assets=[my_cool_asset, my_cooler_asset],
        run_config=asset_configs["some_config.yaml"],
    )

    assert materialization.success
    assert materialization.output_for_node("my_cool_asset") == "Hello, Dagster"
    assert materialization.output_for_node("my_cooler_asset") == "Hello, Dagster!"
