from dagster_utils.lib.gsheets import gsheets_resource

RESOURCES_DEV = {"utils_gsheets": gsheets_resource}

RESOURCES_PROD = {"utils_gsheets": gsheets_resource}
