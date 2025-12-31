"""
Task A.1: Iterative Binary Search
Write a function binary_search(sorted_list, target) that searches for target in sorted_list.
• Maintain two indices, low and high, delimiting the search interval.
• Compute mid = (low + high) // 2.
• If the element is found, return its index. If the interval becomes empty, return -1.
• Requirement: The implementation must be iterative (using a while loop), not recursive.
"""

"""
Task A.2: Edge Cases and Validation
Binary search is notorious for "off-by-one" errors (infinite loops). Create a rigorous test script using
assertions (assert) to verify your function on:
• An empty list [].
• A list where the target is at the very beginning or very end.
• A list where the target is absent.
• A list with duplicate values.
"""


"""
Task A.3: The Power of Logarithms
Compare the performance of your function against a standard Linear Search (scanning element by
element).
• Generate sorted lists of size N ∈ {104, 105, 106, 107}.
• For each size, perform 100 random searches.
• Measure the average time per search for both algorithms.
Display of results: Output a formatted table showing the massive speedup factor:
1 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
2 PERFORMANCE COMPARISON ( Average of 100 searches )
3 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
4 List Size ( N ) Linear Search ( s ) Binary Search ( s ) Speedup
5 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
6 10 000 0.000450 0.000003 150 x
7 100 000 0.004200 0.000004 1050 x
8 1 000 000 0.041000 0.000005 8200 x
9 10 000 000 0.415000 0.000006 69000 x
10 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
Observation: Notice how the Linear Search time grows by a factor of 10 each step, while the Binary
Search time remains almost constant.
"""