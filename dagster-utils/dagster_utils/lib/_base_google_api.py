from dagster import get_dagster_logger

logger = get_dagster_logger()


class BaseGoogleAPI:
    def __init__(self, auth=None):
        if auth:  # Is none in stubs/tests
            self.headers = {
                "Authorization": f"Bearer {self._generate_access_token(auth)}"
            }

    def _generate_access_token(self, auth) -> str:
        ...
