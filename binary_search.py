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


import random
import timeit

def linear_search(sorted_list, target):
    for index, value in enumerate(sorted_list):
        if value == target:
            return index
    return -1


def performance_comparison():
    N_values = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
    num_searches = 100

    print("=" * 80)
    print("PERFORMANCE COMPARISON ( Average of 100 searches )")
    print("=" * 80)
    print(f"{'List Size (N)':<20} {'Linear Search (s)':<25} {'Binary Search (s)':<25} {'Speedup'}")
    print("-" * 80)

    for N in N_values:
        sorted_list = list(range(N))

        total_linear_time = 0
        total_binary_time = 0

        for _ in range(num_searches):
            target = random.randint(0, N - 1)

            # Time linear search
            start_time = timeit.default_timer()
            linear_search(sorted_list, target)
            total_linear_time += timeit.default_timer() - start_time

            # Time binary search
            start_time = timeit.default_timer()
            binary_search(sorted_list, target)
            total_binary_time += timeit.default_timer() - start_time

        avg_linear = total_linear_time / num_searches
        avg_binary = total_binary_time / num_searches

        speedup = (avg_linear / avg_binary) if avg_binary > 0 else float('inf')

        print(f"{N:<20,d} {avg_linear:<25.6f} {avg_binary:<25.6f} {speedup:,.0f}x")

    print("=" * 80)

# Running the functions:
test_list = (list(range(100)))
test_target = random.randint(0, 99)

binary_search(test_list, test_target)
test_binary_search()
performance_comparison()