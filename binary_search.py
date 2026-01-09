import random
import timeit


def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    steps = 0

    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_list[mid]
        steps += 1

        if mid_value == target:
            return mid, steps  # Return index and step count
        elif target > mid_value:
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps


def test_binary_search():
    # Note: We now access [0] because the function returns (index, steps)

    # Test empty list
    assert binary_search([], 5)[0] == -1

    # Test target at the beginning
    assert binary_search([1, 2, 3, 4, 5], 1)[0] == 0

    # Test target at the end
    assert binary_search([1, 2, 3, 4, 5], 5)[0] == 4

    # Test target absent
    assert binary_search([1, 2, 3, 4, 5], 6)[0] == -1

    # Test list with duplicate values
    assert binary_search([1, 2, 2, 2, 3], 2)[0] in [1, 2, 3]

    print("All tests passed.")


def linear_search(sorted_list, target):
    steps = 0
    for index, value in enumerate(sorted_list):
        steps += 1
        if value == target:
            return index, steps
    return -1, steps


def performance_comparison():
    N_values = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
    num_searches = 100

    print("=" * 115)
    print("PERFORMANCE COMPARISON (Average of 100 searches)")
    print("=" * 115)
    # Updated headers to include Steps
    print(
        f"{'List Size (N)':<15} {'Lin. Time(s)':<15} {'Lin. Steps':<15}"
        f" {'Bin. Time(s)':<15} {'Bin. Steps':<15} {'Speedup'}")
    print("-" * 115)

    for N in N_values:
        sorted_list = list(range(N))

        total_linear_time = 0
        total_binary_time = 0
        total_linear_steps = 0
        total_binary_steps = 0

        for _ in range(num_searches):
            target = random.randint(0, N - 1)

            # Time Linear Search
            start_time = timeit.default_timer()
            _, steps = linear_search(sorted_list, target)
            total_linear_time += timeit.default_timer() - start_time
            total_linear_steps += steps

            # Time Binary Search
            start_time = timeit.default_timer()
            _, steps = binary_search(sorted_list, target)
            total_binary_time += timeit.default_timer() - start_time
            total_binary_steps += steps

        # Calculate Averages
        avg_linear_time = total_linear_time / num_searches
        avg_binary_time = total_binary_time / num_searches
        avg_linear_steps = total_linear_steps / num_searches
        avg_binary_steps = total_binary_steps / num_searches

        if avg_binary_time > 0:
            speedup = avg_linear_time / avg_binary_time
        else:
            speedup = float('inf')

        # Print Row
        print(
f"{N:<15,d} {avg_linear_time:<15.6f} "
                        f"{avg_linear_steps:<15.0f} {avg_binary_time:<15.6f} "
                        f"{avg_binary_steps:<15.0f} {speedup:,.0f}x")

    print("=" * 115)


# Running the functions:
test_binary_search()
performance_comparison()