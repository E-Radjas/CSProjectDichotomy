"""
Task A.1: Iterative Binary Search
Write a function binary_search(sorted_list, target) that searches for target in sorted_list.
• Maintain two indices, low and high, delimiting the search interval.
• Compute mid = (low + high) // 2.
• If the element is found, return its index. If the interval becomes empty, return -1.
• Requirement: The implementation must be iterative (using a while loop), not recursive.
"""

def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_list[mid]

        if mid_value == target:
            return mid
        elif target > mid_value:
            low = mid + 1
        else:
            high = mid - 1

    return -1


"""
Task A.2: Edge Cases and Validation
Binary search is notorious for "off-by-one" errors (infinite loops). Create a rigorous test script using
assertions (assert) to verify your function on:
• An empty list [].
• A list where the target is at the very beginning or very end.
• A list where the target is absent.
• A list with duplicate values.
"""

def test_binary_search():
    # Test empty list
    assert binary_search([], 5) == -1

    # Test target at the beginning
    assert binary_search([1, 2, 3, 4, 5], 1) == 0

    # Test target at the end
    assert binary_search([1, 2, 3, 4, 5], 5) == 4

    # Test target absent
    assert binary_search([1, 2, 3, 4, 5], 6) == -1

    # Test list with duplicate values
    assert binary_search([1, 2, 2, 2, 3], 2) in [1, 2, 3]  # could return any index of the duplicates

    print("All tests passed.")

"""
Task A.3: The Power of Logarithms
Compare the performance of your function against a standard Linear Search (scanning element by
element).
• Generate sorted lists of size N ∈ {10^4, 10^5, 10^6, 10^7}.
• For each size, perform 100 random searches.
• Measure the average time per search for both algorithms.
Display of results: Output a formatted table showing the massive speedup factor:
1 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
2 PERFORMANCE COMPARISON ( Average of 100 searches )
3 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
4 List Size ( N ) Linear Search ( s ) Binary Search ( s ) Speedup
5 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
6 10 000 0.000450 0.000003 150 x
7 100 000 0.004200 0.000004 1050 x
8 1 000 000 0.041000 0.000005 8200 x
9 10 000 000 0.415000 0.000006 69000 x
10 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
Observation: Notice how the Linear Search time grows by a factor of 10 each step, while the Binary
Search time remains almost constant.
"""

import timeit
import random
def linear_search(sorted_list, target):
    for index, value in enumerate(sorted_list):
        if value == target:
            return index
    return -1

import timeit
import random


def linear_search(sorted_list, target):
    for index, value in enumerate(sorted_list):
        if value == target:
            return index
    return -1


def performance_comparison():
    sizes = [10_000, 100_000, 1_000_000, 10_000_000]
    results = []

    for n in sizes:
        data = list(range(n))

        linear_avg = timeit.Timer(
            "linear_search(data, random.randrange(n))",
            globals={"linear_search": linear_search, "data": data, "random": random, "n": n},
        ).timeit(number=100) / 100

        binary_avg = timeit.Timer(
            "binary_search(data, random.randrange(n))",
            globals={"binary_search": binary_search, "data": data, "random": random, "n": n},
        ).timeit(number=100) / 100

        results.append((n, linear_avg, binary_avg))

    return results

def performance_comparison_table():
    print(f"""{"="*110}
    PERFORMANCE COMPARISON (Average of 100 searches)
    {"="*110}
    {'List Size (N)':<15}{'Linear Search (s)':>20}{'Binary Search (s)':>20}{'Speedup':>15}
    {'-'*70}
    {10000:>15,}{linear_search_average_104:>20.6f}{binary_search_average_104:>20.6f}{(linear_search_average_104/binary_search_average_104):>14.0f}x
    {100000:>15,}{linear_search_average_105:>20.6f}{binary_search_average_105:>20.6f}{(linear_search_average_105/binary_search_average_105):>14.0f}x
    {1000000:>15,}{linear_search_average_106:>20.6f}{binary_search_average_106:>20.6f}{(linear_search_average_106/binary_search_average_106):>14.0f}x
    {10000000:>15,}{linear_search_average_107:>20.6f}{binary_search_average_107:>20.6f}{(linear_search_average_107/binary_search_average_107):>14.0f}x
    {"="*110}
    """)

performance_comparison()