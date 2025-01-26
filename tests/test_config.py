import pytest
from clickup_cli.config import get_config


def test_get_config(mocker):
    mocker.patch.dict(
        "os.environ",
        {
            "CLICKUP_API_TOKEN": "mock_token",
            "CLICKUP_TEAM_ID": "mock_team",
            "CLICKUP_USER_ID": "mock_user",
        },
    )

    config = get_config()
    assert config["CLICKUP_API_TOKEN"] == "mock_token"
    assert config["CLICKUP_TEAM_ID"] == "mock_team"
    assert config["CLICKUP_USER_ID"] == "mock_user"
