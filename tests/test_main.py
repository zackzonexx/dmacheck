import unittest
import sys
from package.main import main


class TestMain(unittest.TestCase):
    def test_main_function(self):
        # Call the main function and check if it runs without errors
        with self.assertRaises(SystemExit) as cm:
            main()

        # Check if the exit status code is 1
        self.assertEqual(cm.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
