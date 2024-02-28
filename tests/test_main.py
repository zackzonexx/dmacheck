import unittest
from package.main import main


class TestMain(unittest.TestCase):
    def test_main_function(self):
        # Call the main function and check if it runs without errors
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised an unexpected exception: {e}")


if __name__ == "__main__":
    unittest.main()
