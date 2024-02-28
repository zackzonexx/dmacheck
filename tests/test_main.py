import unittest
from unittest.mock import patch, MagicMock
from package.main import main


class TestMain(unittest.TestCase):

    @patch("package.main.get_muted_alerts")
    @patch("package.main.build")
    @patch("package.main.service_account.Credentials.from_service_account_file")
    def test_main_function(self, mock_credentials, mock_build, mock_get_muted_alerts):
        # Mocking return values for dependencies
        mock_credentials.return_value = None
        mock_build.return_value.spreadsheets.return_value.values.return_value.append.return_value.execute.return_value = (
            None
        )
        mock_get_muted_alerts.return_value = {"priority 1": ["id1", "id2"]}

        # Call the main function
        main()

        # Add assertions as needed

    @patch("package.main.sys.stderr", MagicMock())
    def test_main_function_with_missing_args(self):
        # Test the main function with missing arguments
        with self.assertRaises(SystemExit) as cm:
            # Pass an empty list of arguments
            with patch("sys.argv", [""]):
                main()

        # Assert that the script exits with status code 2
        self.assertEqual(cm.exception.code, 2)

    @patch("package.main.get_muted_alerts", return_value={})
    @patch("package.main.build")
    @patch("package.main.service_account.Credentials.from_service_account_file")
    def test_main_function_no_muted_alerts(
        self, mock_credentials, mock_build, mock_get_muted_alerts
    ):
        # Mocking return values for dependencies
        mock_credentials.return_value = None
        mock_build.return_value.spreadsheets.return_value.values.return_value.append.return_value.execute.return_value = (
            None
        )

        # Call the main function
        main()

        # Add assertions as needed


if __name__ == "__main__":
    unittest.main()
