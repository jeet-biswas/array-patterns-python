def count_arithmetic_subsequences(values: list[int]) -> int:
    """Count index-distinct arithmetic subsequences of length >= 3, exactly; no mutation."""
    states = [{} for _ in values]
    total = 0
    for i, value in enumerate(values):
        for j in range(i):
            difference = value-values[j]
            extensions = states[j].get(difference, 0)
            total += extensions
            states[i][difference] = states[i].get(difference, 0) + extensions + 1
    return total
