import os

from dagster import build_init_resource_context, build_op_context

from dagster_utils.lib.gsheets import (
    UtilsGSheetsClient,
    fetch_from_gsheets,
    gsheets_resource,
    stub_gsheets_resource,
)
from dagster_utils.lib.types import UtilsFileSystemOutputType

STUBS_DIR = os.path.join(os.path.dirname(__file__), "_stubs", "gsheets")

# Dagster tests
def test_gsheets_resource_init(mock_fetch_auth):
    with build_init_resource_context() as context:
        resource = gsheets_resource(context)

    assert type(resource) is UtilsGSheetsClient


def test_fetch_from_gsheets():
    context = build_op_context(
        config={"sheet_mapping": {"some_key": "some_id"}},
        resources={
            "gsheets": stub_gsheets_resource.configured({"stubs_dir": STUBS_DIR})
        },
    )

    assert fetch_from_gsheets(context) == [
        UtilsFileSystemOutputType(
            filename="some_key.csv",
            content=b"my;cool;csv\n1;2;3\n1;2;3",
        )
    ]
