# import the built-in test runner module "unittest":
import unittest

# this is how you define a class that extends another class in Python:
class TestSum(unittest.TestCase):
    # "self" is equivalent to "this" in JS. The unittest.TestCase class has assertion methods that one must use when using the unittest test runner
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

# when unittest.main() is called, it will call the methods on classes that extend the unittest.TestCase class.