from dagster import materialize_to_memory
from dagster_utils.lib.gsheets import stub_gsheets_resource
from dagster_utils.lib.types import UtilsFileSystemOutputType

from some_dagster_project.assets.some_gsheets_asset import *

STUBS_DIR = os.path.join(os.path.dirname(__file__), "_stub")


def test_cool_assets(asset_configs):
    materialization = materialize_to_memory(
        assets=[my_gsheets_asset],
        run_config=asset_configs["some_gsheets_config.yaml"],
        resources={
            "utils_gsheets": stub_gsheets_resource.configured({"stubs_dir": STUBS_DIR}),
        },
    )

    assert materialization.success
    assert materialization.output_for_node("my_gsheets_asset") == [
        UtilsFileSystemOutputType(
            filename="my_cool_sheet.csv", content=b"1;2;3\na;b;c"
        ),
        UtilsFileSystemOutputType(
            filename="my_cooler_sheet.csv", content=b"1;2;3\na;b;c"
        ),
    ]
