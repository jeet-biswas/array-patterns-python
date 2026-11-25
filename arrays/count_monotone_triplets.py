def count_monotone_triplets(values: list[int]) -> int:
    """Count i<j<k with values strictly increasing or decreasing; no mutation."""
    total = 0
    for j, value in enumerate(values):
        left_low = left_high = right_low = right_high = 0
        for i in range(j):
            left_low += values[i] < value
            left_high += values[i] > value
        for k in range(j+1, len(values)):
            right_low += values[k] < value
            right_high += values[k] > value
        total += left_low*right_high+left_high*right_low
    return total
