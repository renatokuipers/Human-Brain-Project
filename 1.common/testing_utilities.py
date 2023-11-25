# Tools and frameworks for conducting tests on the modules

import unittest

def run_tests(test_classes):
    """Run a suite of unittests.

    Args:
        test_classes (list): List of unittest.TestCase classes to run.
    """
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    
    big_suite = unittest.TestSuite(suites_list)
    runner = unittest.TextTestRunner()
    runner.run(big_suite)

class AssertAlmostEqualMixin:
    """Mixin class to add assertAlmostEqual for iterables in unittests."""
    def assertIterableAlmostEqual(self, first, second, places=7, msg=None):
        self.assertEqual(len(first), len(second), msg="Length of iterables is not equal")
        for a, b in zip(first, second):
            self.assertAlmostEqual(a, b, places=places, msg=msg)

# Example usage of AssertAlmostEqualMixin in a test case:
class MyTestCase(unittest.TestCase, AssertAlmostEqualMixin):
    def test_similar_iterables(self):
        self.assertIterableAlmostEqual([0.1, 0.2, 0.3], [0.1, 0.2, 0.3000001])
