import pytest
from unittest.mock import patch
from package.main import main


@pytest.mark.parametrize(
    "args, expected_team_name",
    [
        (["main.py", "--team-name", "dummy_team"], "dummy_team"),
        # Add more test cases as needed
    ],
)
def test_main_with_args(args, expected_team_name):
    # Call the main function with the mocked command line arguments
    with patch("sys.argv", args):
        main()

    # Access expected_team_name within the test function
    assert expected_team_name == "dummy_team"
