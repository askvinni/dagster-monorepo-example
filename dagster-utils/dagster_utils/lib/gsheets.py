import os

import requests
from dagster import Field, List, Out, get_dagster_logger, op, resource

from dagster_utils.lib.types import UtilsFileSystemOutputType

from ._base_google_api import BaseGoogleAPI
from ._mock_requests_response import MockRequestResponse

logger = get_dagster_logger()


# ###############################
# DAGSTER SPECIFIC
# ###############################


@resource(config_schema={"auth": dict})
def gsheets_resource(init_context):
    return UtilsGSheetsClient(init_context.resource_config)


@op(
    description=str(
        "Fetches data from a Google Sheets source. Returns a list of `UtilsFileSystemOutputType` "
        "with the provided key in the `sheet_mapping` as the `filename` property (csv), "
        "and the spreadsheet bytes-like content as the `content` property."
    ),
    required_resource_keys={"gsheets"},
    config_schema={"sheet_mapping": dict},
    out=Out(dagster_type=List[UtilsFileSystemOutputType]),
)
def fetch_from_gsheets(context) -> List[UtilsFileSystemOutputType]:
    return context.resources.gsheets.fetch_sheets_as_csv(context.op_config)


# ###############################
# API LIB
# ###############################


class UtilsGSheetsClient(BaseGoogleAPI):
    def __init__(self, config):
        super().__init__(config)

    def fetch_sheets_as_csv(self, options) -> List[UtilsFileSystemOutputType]:
        res = []
        for key, sheet_id in options.get("sheet_mapping").items():
            res.append(
                UtilsFileSystemOutputType(
                    filename=f"{key}.csv",
                    content=self._fetch_sheet_as_csv(sheet_id).content,
                )
            )

        return res

    def _fetch_sheet_as_csv(self, sheet_id) -> requests.Response:
        return requests.get(
            f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&",
            headers=self.headers,
        )


# ###############################
# STUB
# ###############################


@resource(config_schema={"stubs_dir": Field(str, is_required=False)})
def stub_gsheets_resource(context):
    return StubUtilsGSheetsClient(context.resource_config.get("stubs_dir"))


class StubUtilsGSheetsClient(UtilsGSheetsClient):
    def __init__(self, stubs_dir):
        super().__init__({})
        self.stubs_dir = stubs_dir

    def _generate_access_token(self) -> str:
        return ""

    def _fetch_sheet_as_csv(self, sheet_id) -> requests.Response:
        with open(os.path.join(self.stubs_dir, f"{sheet_id}.csv"), "rb") as f:
            return MockRequestResponse(content=f.read())
