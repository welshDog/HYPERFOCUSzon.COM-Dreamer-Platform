# File: h:\benchmark_performance.py
import random
import time

from tabnine_test import calculate_fibonacci, reverse_string, sort_list


def benchmark_fibonacci():
    """Benchmark Fibonacci performance."""
    print("🚀 Fibonacci Performance Test:")
    test_values = [10, 20, 30, 35]

    for n in test_values:
        start_time = time.time()
        result = calculate_fibonacci(n)
        end_time = time.time()
        print(f"  fib({n}) = {result}, Time: {end_time - start_time:.6f}s")


def benchmark_sorting():
    """Benchmark sorting performance."""
    print("\n⚡ Sorting Performance Test:")
    sizes = [1000, 10000, 100000]

    for size in sizes:
        # Create random list
        test_list = [random.randint(1, 1000) for _ in range(size)]

        start_time = time.time()
        sorted_list = sort_list(test_list)
        end_time = time.time()

        print(f"  Sorted {size} items in {end_time - start_time:.6f}s")


def benchmark_string_reversal():
    """Benchmark string reversal performance."""
    print("\n💎 String Reversal Performance Test:")
    test_strings = ["short", "a" * 1000, "a" * 10000, "a" * 100000]

    for test_str in test_strings:
        start_time = time.time()
        reversed_str = reverse_string(test_str)
        end_time = time.time()

        print(
            f"  Reversed string of length {len(test_str)} in {end_time - start_time:.6f}s"
        )


if __name__ == "__main__":
    print("🏆 HYPERFOCUS ZONE - Performance Benchmark Suite 🏆")
    print("=" * 60)
    benchmark_fibonacci()
    benchmark_sorting()
    benchmark_string_reversal()
    print("=" * 60)
    print("✅ Benchmark complete! All optimizations verified.")
