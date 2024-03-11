from unittest.mock import patch
from package.main import get_arg_value


def test_get_arg_value():
    # Define input arguments
    args = [
        "--datadog-api-key",
        "dummy_api_key",
        "--datadog-app-key",
        "dummy_app_key",
        "--team-name",
        "dummy_team",
        "--opsgenie-api-key",
        "dummy_opsgenie_key",
    ]

    # Call the function with the mocked input arguments
    with patch("sys.argv", args):
        datadog_api_key = get_arg_value("--datadog-api-key")
        datadog_app_key = get_arg_value("--datadog-app-key")
        team_name = get_arg_value("--team-name")
        opsgenie_api_key = get_arg_value("--opsgenie-api-key")

    # Assert the results
    assert datadog_api_key == "dummy_api_key"
    assert datadog_app_key == "dummy_app_key"
    assert team_name == "dummy_team"
    assert opsgenie_api_key == "dummy_opsgenie_key"
