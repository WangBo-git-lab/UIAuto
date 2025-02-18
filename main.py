import unittest
from tests.test_icon_click import TestIconClick
from tests.test_check_courselist import TestHomepageSlideClick

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIconClick))
    suite.addTest(unittest.makeSuite(TestHomepageSlideClick))
    runner = unittest.TextTestRunner()
    runner.run(suite)