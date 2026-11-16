def arithmetic_slices(values: list[int]) -> int:
    """Count contiguous constant-difference subarrays of length at least three.

    O(n) time and O(1) space; input is unchanged.
    """
    ending = total = 0
    for i in range(2, len(values)):
        if values[i] - values[i-1] == values[i-1] - values[i-2]:
            ending += 1
        else:
            ending = 0
        total += ending
    return total
