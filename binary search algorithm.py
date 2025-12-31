"""
1 : demander target, low et high number
2 : construire la liste sorted avec pour borne : low and high
3 : calculer la moyenne de la liste
4 : faire boucle while pour trouver si le target est dans la 1ʳᵉ moitie ou dans la 2e
5 : Dans la boucle, si c'est dans la 1ʳᵉ moitie, réduire la borne high jusqu'à mid
6 : Faire de meme pour cas contraire
7 : Faire dans la boucle un compteur pour savoir combien de boucle, il a fallu pour trouver le target
8 : Dans la boucle, si target trouver, finir la boucle en annonçant le nombre target et le total de
    boucle demander pour le trouver
9 :
"""

def read_int(prompt: str) -> int:
    """Read an integer from the user."""
    return int(input(prompt))


def get_search_params() -> tuple[int, int, int]:
    """Ask for target, low, and high."""
    target = read_int("Give a target number: ")
    low = read_int("Give a lower number: ")
    high = read_int("Give a higher number: ")

    if low > high:
        low, high = high, low  # normalize bounds

    return target, low, high


def build_sorted_range(low: int, high: int) -> list[int]:
    """Construct the sorted list with bounds low and high (inclusive)."""
    return list(range(low, high + 1))


def binary_search_steps(values: list[int], target: int) -> tuple[bool, int, int]:
    """
    Binary search in a sorted list.
    Returns: (found, index, steps). index is -1 when not found.
    """
    left = 0
    right = len(values) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2
        mid_value = values[mid]

        if mid_value == target:
            return True, mid, steps
        if target > mid_value:
            left = mid + 1
        else:
            right = mid - 1

    return False, -1, steps


def main() -> None:
    target, low, high = get_search_params()
    values = build_sorted_range(low, high)

    found, index, steps = binary_search_steps(values, target)

    if found:
        print(f"Target {target} found at index {index} in {steps} step(s).")
    else:
        print(f"Target {target} not found in range [{low}, {high}] after {steps} step(s).")


if __name__ == "__main__":
    main()
