def count_target_quadruplets(values: list[int], target: int) -> int:
    """Count i<j<k<l whose four values sum to target; no mutation."""
    pairs = {}
    total = 0
    for third in range(2, len(values)-1):
        second = third-1
        for first in range(second):
            value = values[first]+values[second]
            pairs[value] = pairs.get(value, 0)+1
        for fourth in range(third+1, len(values)):
            total += pairs.get(target-values[third]-values[fourth], 0)
    return total
