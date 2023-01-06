import os

from dagster import DefaultSensorStatus
from dagster_slack import make_slack_on_run_failure_sensor


def slack_message_fn(context) -> str:
    return (
        f":daggy-fail: Job {context.pipeline_run.pipeline_name} failed! :daggy-fail:\n"
        f"Error: {context.failure_event.message}"
    )


slack_on_run_failure = make_slack_on_run_failure_sensor(
    channel="my_channel",
    slack_token=os.getenv("SLACK_TOKEN"),
    text_fn=slack_message_fn,
    dagit_base_url="htts://some-cool-url.cloud",
    default_status=DefaultSensorStatus.RUNNING,
)
