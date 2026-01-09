"""
Binary Search vs Linear Search Performance Comparison Module.

This module demonstrates the efficiency difference between binary search (O(log n))
and linear search (O(n)) algorithms through benchmarking.
"""
import random
import timeit


def binary_search(sorted_list, target):
    """
    Perform binary search on a sorted list to find a target value.

    Uses the divide-and-conquer approach by repeatedly halving the search space,
    resulting in O(log n) time complexity.

    Args:
        sorted_list: A list sorted in ascending order.
        target: The value to search for.

    Returns:
        A tuple of (index, steps) where:
            - index: Position of target in list, or -1 if not found.
            - steps: Number of iterations performed.
    """
    low = 0
    high = len(sorted_list) - 1
    steps = 0

    while low <= high:
        # Use integer division to find the midpoint, avoiding overflow
        mid = (low + high) // 2
        mid_value = sorted_list[mid]
        steps += 1

        if mid_value == target:
            return mid, steps
        elif target > mid_value:
            # Target is in the upper half; discard lower half
            low = mid + 1
        else:
            # Target is in the lower half; discard upper half
            high = mid - 1

    return -1, steps


def test_binary_search():
    """
    Run unit tests to verify binary_search correctness.

    Tests cover edge cases: empty list, target at boundaries,
    absent target, and duplicate values.
    """
    # Access [0] because binary_search returns (index, steps) tuple

    # Test empty list
    assert binary_search([], 5)[0] == -1

    # Test target at the beginning
    assert binary_search([1, 2, 3, 4, 5], 1)[0] == 0

    # Test target at the end
    assert binary_search([1, 2, 3, 4, 5], 5)[0] == 4

    # Test target absent
    assert binary_search([1, 2, 3, 4, 5], 6)[0] == -1

    # With duplicates, any valid index containing the target is acceptable
    assert binary_search([1, 2, 2, 2, 3], 2)[0] in [1, 2, 3]

    print("All tests passed.")


def linear_search(sorted_list, target):
    """
    Perform linear search by checking each element sequentially.

    This O(n) algorithm serves as a baseline for comparing against binary search.

    Args:
        sorted_list: A list to search through (sorting not required).
        target: The value to search for.

    Returns:
        A tuple of (index, steps) where:
            - index: Position of target in list, or -1 if not found.
            - steps: Number of elements examined.
    """
    steps = 0
    for index, value in enumerate(sorted_list):
        steps += 1
        if value == target:
            return index, steps
    return -1, steps


def performance_comparison():
    """
    Benchmark binary search vs linear search across varying list sizes.

    Runs multiple searches for each list size and reports average
    execution time, step count, and relative speedup.
    """
    list_sizes = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
    num_searches = 100

    print("=" * 115)
    print("PERFORMANCE COMPARISON (Average of 100 searches)")
    print("=" * 115)
    print(
        f"{'List Size (N)':<15} {'Lin. Time(s)':<15} {'Lin. Steps':<15}"
        f" {'Bin. Time(s)':<15} {'Bin. Steps':<15} {'Speedup'}")
    print("-" * 115)

    for size in list_sizes:
        sorted_list = list(range(size))

        total_linear_time = 0
        total_binary_time = 0
        total_linear_steps = 0
        total_binary_steps = 0

        for search_index in range(num_searches):
            target = random.randint(0, size - 1)

            # Time Linear Search
            start_time = timeit.default_timer()
            search_index, steps = linear_search(sorted_list, target)
            total_linear_time += timeit.default_timer() - start_time
            total_linear_steps += steps

            # Time Binary Search
            start_time = timeit.default_timer()
            search_index, steps = binary_search(sorted_list, target)
            total_binary_time += timeit.default_timer() - start_time
            total_binary_steps += steps

        # Calculate Averages
        avg_linear_time = total_linear_time / num_searches
        avg_binary_time = total_binary_time / num_searches
        avg_linear_steps = total_linear_steps / num_searches
        avg_binary_steps = total_binary_steps / num_searches

        # Avoid division by zero for extremely fast operations
        if avg_binary_time > 0:
            speedup = avg_linear_time / avg_binary_time
        else:
            speedup = float('inf')

        # Print Row
        print(
f"{size:<15,d} {avg_linear_time:<15.6f} "
                        f"{avg_linear_steps:<15.0f} {avg_binary_time:<15.6f} "
                        f"{avg_binary_steps:<15.0f} {speedup:,.0f}x")

    print("=" * 115)

# Output example:
# ===================================================================================================================
# PERFORMANCE COMPARISON (Average of 100 searches)
# ===================================================================================================================
# List Size (N)   Lin. Time(s)    Lin. Steps      Bin. Time(s)    Bin. Steps      Speedup
# -------------------------------------------------------------------------------------------------------------------
# 10,000          0.000437        5110            0.000003        12              145x
# 100,000         0.004102        47954           0.000005        16              815x
# 1,000,000       0.037405        478756          0.000008        19              4,663x
# 10,000,000      0.368110        4737077         0.000011        22              33,501x
# ===================================================================================================================


def generate_tikz(sorted_list, target):
    """
    Generate TikZ/LaTeX code to visualize binary search steps for Beamer presentations.


    Creates animated slides showing how binary search progressively narrows down
    the search space. Each step highlights the current mid element and grays out
    eliminated portions of the list.

    Args:
        sorted_list: A list sorted in ascending order to visualize the search on.
        target: The value being searched for in the visualization.

    Returns:
        None. Outputs TikZ code directly to stdout for use in LaTeX documents.
    """

    low = 0
    high = len(sorted_list) - 1
    step = 1  # Beamer slide counter for overlay specifications <1>, <2>, etc.

    # TikZ preamble: set up the drawing environment and node styles
    print(r"% Code automatically generated by Python")
    print(r"\begin{tikzpicture}[scale=0.8, transform shape]")
    print(r"  % Nodes style")
    print(r"  \tikzstyle{mybox} = [draw, minimum size=0.8cm, align=center]")

    # Generate one overlay frame per binary search iteration
    while low <= high:
        mid = (low + high) // 2

        # Start Beamer overlay block for this step
        print(f"  \\only<{step}>{{")

        # Render each list element with appropriate visual styling
        for i, val in enumerate(sorted_list):
            # Color coding: orange for current mid, gray for eliminated, white for active
            if i == mid:
                color_opt = "fill=orange!50"
            elif i < low or i > high:
                color_opt = "fill=gray!30, text=gray"
            else:
                color_opt = "fill=white"

            # Draw the value box
            print(f"    \\node[mybox, {color_opt}] at ({i}, 0) {{{val}}};")
            # Draw the index label below each box
            print(f"    \\node[font=\\tiny, text=gray] at ({i}, -0.6) {{{i}}};")

        # Display current search state information below the array
        print(
            f"    \\node[anchor=north] at ({len(sorted_list)/2}, -1.5) "
            f"{{Step {step}: low={low}, high={high}, mid={mid} "
            f"(Value: {sorted_list[mid]})}};"
        )

        print("  }")

        # Standard binary search logic to narrow the search space
        if sorted_list[mid] == target:
            break
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

        step += 1

    print(r"\end{tikzpicture}")

print("-" * 50)

demonstration_list = [14, 25, 31, 46, 52, 63, 71, 84, 96, 99]
target = 71

generate_tikz(demonstration_list, target)

print("-" * 50)


# Running the functions:
test_binary_search()
performance_comparison()
