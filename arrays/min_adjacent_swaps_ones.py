def min_adjacent_swaps_ones(values: list[int]) -> int:
    """Fewest adjacent swaps grouping all ones into a single linear block.

    Binary input required (ValueError otherwise). Empty/no ones -> 0.
    O(n) time, O(n) space; input is unchanged. No circular wrapping.
    """
    if any(value not in (0, 1) for value in values):
        raise ValueError('values must contain only zero and one')
    adjusted = []
    for i, value in enumerate(values):
        if value:
            adjusted.append(i - len(adjusted))
    if not adjusted:
        return 0
    median = adjusted[len(adjusted) // 2]
    return sum(abs(position - median) for position in adjusted)
