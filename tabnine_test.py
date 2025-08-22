# Test file for Tabnine AI completion
# Start typing and see Tabnine suggestions


def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number using memoization for optimization."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n

    # Use memoization for better performance
    memo = {0: 0, 1: 1}

    def fib_helper(num):
        if num in memo:
            return memo[num]
        memo[num] = fib_helper(num - 1) + fib_helper(num - 2)
        return memo[num]

    return fib_helper(n)


def sort_list(items):
    """Sort a list efficiently using Python's built-in Timsort algorithm."""
    if not items:
        return []
    return sorted(items)


def reverse_string(text):
    """Reverse a string efficiently using slicing."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]
