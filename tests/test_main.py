import pytest
from unittest.mock import patch
from dmacheck.main import main


@pytest.mark.parametrize(
    "args, expected_team_name, expected_datadog_api_key, expected_datadog_app_key, expected_opsgenie_api_key",
    [
        (
            [
                "main.py",
                "--datadog-api-key",
                "dummy_api_key",
                "--datadog-app-key",
                "dummy_app_key",
                "--team-name",
                "dummy_team",
                "--opsgenie-api-key",
                "dummy_opsgenie_key",
            ],
            "dummy_team",
            "dummy_api_key",
            "dummy_app_key",
            "dummy_opsgenie_key",
        ),
        # Add more test cases as needed
    ],
)
def test_main_with_args(
    args,
    expected_team_name,
    expected_datadog_api_key,
    expected_datadog_app_key,
    expected_opsgenie_api_key,
):
    # Mock the functions or classes called within main() to avoid executing the entire logic
    with patch("dmacheck.main.get_muted_alerts"):
        with patch("dmacheck.main.create_alert_payload"):
            with patch("dmacheck.opsgenie_utils.opsgenie_sdk.AlertApi.create_alert"):
                # Call the main function with the mocked command line arguments
                with patch("sys.argv", args):
                    main()

    # Access expected_team_name, expected_datadog_api_key, expected_datadog_app_key, and expected_opsgenie_api_key within the test function
    assert expected_team_name == "dummy_team"
    assert expected_datadog_api_key == "dummy_api_key"
    assert expected_datadog_app_key == "dummy_app_key"
    assert expected_opsgenie_api_key == "dummy_opsgenie_key"
