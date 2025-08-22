# File: h:\test_tabnine_functions.py
import os
import sys
import unittest

# Add the directory containing your module to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tabnine_test import calculate_fibonacci, reverse_string, sort_list


class TestTabnineFunctions(unittest.TestCase):

    def test_calculate_fibonacci(self):
        """Test Fibonacci calculation with various inputs."""
        # Test base cases
        self.assertEqual(calculate_fibonacci(0), 0)
        self.assertEqual(calculate_fibonacci(1), 1)

        # Test known values
        self.assertEqual(calculate_fibonacci(2), 1)
        self.assertEqual(calculate_fibonacci(3), 2)
        self.assertEqual(calculate_fibonacci(4), 3)
        self.assertEqual(calculate_fibonacci(5), 5)
        self.assertEqual(calculate_fibonacci(10), 55)

        # Test larger values
        self.assertEqual(calculate_fibonacci(20), 6765)

        # Test error cases
        with self.assertRaises(ValueError):
            calculate_fibonacci(-1)

    def test_sort_list(self):
        """Test list sorting functionality."""
        # Test empty list
        self.assertEqual(sort_list([]), [])

        # Test single element
        self.assertEqual(sort_list([5]), [5])

        # Test already sorted
        self.assertEqual(sort_list([1, 2, 3, 4]), [1, 2, 3, 4])

        # Test reverse sorted
        self.assertEqual(sort_list([4, 3, 2, 1]), [1, 2, 3, 4])

        # Test random order
        self.assertEqual(sort_list([3, 1, 4, 1, 5, 9]), [1, 1, 3, 4, 5, 9])

        # Test with strings
        self.assertEqual(sort_list(["c", "a", "b"]), ["a", "b", "c"])

        # Test with mixed types (should work in Python 2, may raise TypeError in Python 3)
        try:
            result = sort_list([1, "a", 2])
        except TypeError:
            pass  # Expected in Python 3

    def test_reverse_string(self):
        """Test string reversal functionality."""
        # Test empty string
        self.assertEqual(reverse_string(""), "")

        # Test single character
        self.assertEqual(reverse_string("a"), "a")

        # Test normal strings
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")

        # Test palindromes
        self.assertEqual(reverse_string("racecar"), "racecar")

        # Test with spaces and special characters
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string("a!b@c#"), "#c@b!a")

        # Test error cases
        with self.assertRaises(TypeError):
            reverse_string(123)
        with self.assertRaises(TypeError):
            reverse_string(None)


class TestPerformance(unittest.TestCase):
    """Performance tests to ensure optimizations work."""

    def test_fibonacci_performance(self):
        """Test that Fibonacci can handle moderately large inputs quickly."""
        import time

        start_time = time.time()
        result = calculate_fibonacci(30)
        end_time = time.time()

        self.assertEqual(result, 832040)
        # Should complete in well under a second with memoization
        self.assertLess(end_time - start_time, 1.0)

    def test_sort_large_list(self):
        """Test sorting performance with larger lists."""
        import random

        # Create a large random list
        large_list = [random.randint(1, 1000) for _ in range(10000)]

        import time

        start_time = time.time()
        sorted_list = sort_list(large_list)
        end_time = time.time()

        # Verify it's actually sorted
        self.assertEqual(sorted_list, sorted(large_list))
        # Should complete quickly
        self.assertLess(end_time - start_time, 1.0)


if __name__ == "__main__":
    # Run tests with verbose output
    unittest.main(verbosity=2)
