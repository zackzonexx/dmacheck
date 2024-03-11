import unittest
from unittest.mock import patch
from package.main import main


class TestMain(unittest.TestCase):
    @patch(
        "sys.argv",
        [
            "main.py",
            "--datadog-api-key",
            "YOUR_DATADOG_API_KEY",
            "--datadog-app-key",
            "YOUR_DATADOG_APP_KEY",
            "--team-name",
            "YOUR_TEAM_NAME",
            "--opsgenie-api-key",
            "YOUR_OPSGENIE_API_KEY",
        ],
    )
    def test_main_function(self):
        # Call the main function and check if it runs without errors
        with self.assertRaises(SystemExit) as cm:
            main()

        # Check if the exit status code is 0 (no errors expected)
        self.assertEqual(cm.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
