def min_swaps_group_ones(values: list[int]) -> int:
    """Minimum swaps of any two indices to make all ones contiguous.

    Accepts only 0 and 1 (ValueError otherwise). Empty/no ones -> 0.
    This is not an adjacent-swap or circular-array problem.
    O(n) time and O(1) space; input is unchanged.
    """
    if any(value not in (0, 1) for value in values):
        raise ValueError('only 0 and 1 are accepted')
    width = sum(values)
    if width < 2:
        return 0
    inside = sum(values[i] for i in range(width))
    most = inside
    for right in range(width, len(values)):
        inside += values[right] - values[right - width]
        most = max(most, inside)
    return width - most
