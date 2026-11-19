def min_cost_equal_weighted(values: list[int], weights: list[int]) -> int:
    """Minimize sum(weights[i]*abs(values[i]-target)) over integer targets.

    Equal lengths and nonnegative weights required, else ValueError.
    Empty/all-zero weights -> 0. O(n log n) time, O(n) space; no mutation.
    """
    if len(values) != len(weights) or any(weight < 0 for weight in weights):
        raise ValueError('equal lengths and nonnegative weights are required')
    total = sum(weights)
    if total == 0:
        return 0
    cumulative = 0
    for value, weight in sorted(zip(values, weights)):
        cumulative += weight
        if cumulative * 2 >= total:
            median = value
            break
    return sum(weight * abs(value - median) for value, weight in zip(values, weights))
