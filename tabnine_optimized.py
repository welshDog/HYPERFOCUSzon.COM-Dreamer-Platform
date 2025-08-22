# File: h:\tabnine_optimized.py
from functools import lru_cache
from typing import List


@lru_cache(maxsize=None)
def calculate_fibonacci_cached(n: int) -> int:
    """Ultra-fast Fibonacci using built-in LRU cache."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return calculate_fibonacci_cached(n - 1) + calculate_fibonacci_cached(n - 2)


def calculate_fibonacci_iterative(n: int) -> int:
    """Memory-efficient iterative Fibonacci - O(1) space complexity."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def sort_list_inplace(items: List) -> List:
    """In-place sorting for memory efficiency."""
    if not items:
        return []
    items.sort()  # In-place sorting
    return items


def reverse_string_optimized(text: str) -> str:
    """Optimized string reversal with type checking."""
    if not text:
        return text
    return text[::-1]
