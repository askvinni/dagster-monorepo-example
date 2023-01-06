from dagster import IOManager, io_manager


@io_manager(
    config_schema={...},
    required_resource_keys={...},
)
def dagster_utils_s3_io_manager(init_context):
    return UtilsIOManager(init_context)


class UtilsIOManager(IOManager):
    ...
