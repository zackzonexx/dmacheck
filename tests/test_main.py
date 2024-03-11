import unittest
from unittest.mock import patch, MagicMock
from package.main import main


class TestMain(unittest.TestCase):
    @patch(
        "sys.argv",
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
    )
    @patch("package.main.get_muted_alerts")
    @patch("package.main.create_alert_payload")
    @patch("package.opsgenie_utils.opsgenie_sdk.AlertApi.create_alert")
    def test_main_function(
        self, mock_create_alert, mock_create_alert_payload, mock_get_muted_alerts
    ):
        # Mocking return values
        mock_get_muted_alerts.return_value = {
            "alert1": ["123", "456"],
            "alert2": ["789"],
        }

        # Mocking the alert payload creation
        mock_create_alert_payload.return_value = MagicMock()

        # Mocking the Opsgenie API client and its create_alert method
        mock_client = MagicMock()
        mock_create_alert.return_value = MagicMock()

        # Call the main function
        main()

        # Check if get_muted_alerts was called with correct arguments
        mock_get_muted_alerts.assert_called_once_with(
            "dummy_api_key", "dummy_app_key", "dummy_team"
        )

        # Check if create_alert_payload was called with correct arguments
        mock_create_alert_payload.assert_any_call("alert1", ["123", "456"])
        mock_create_alert_payload.assert_any_call("alert2", ["789"])

        # Check if create_alert method of the Opsgenie API client was called
        mock_create_alert.assert_called_once()

        # Check if the call to create_alert method was made with the correct alert payload
        args, kwargs = mock_create_alert.call_args
        self.assertIsNotNone(kwargs["alert_payload"])


if __name__ == "__main__":
    unittest.main()
