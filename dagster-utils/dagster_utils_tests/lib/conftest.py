import pytest

from dagster_utils.lib._base_google_api import BaseGoogleAPI


@pytest.fixture
def mock_fetch_auth(monkeypatch):
    def mock_access_token(*args, **kwargs):
        return ""

    monkeypatch.setattr(BaseGoogleAPI, "_generate_access_token", mock_access_token)
