def maximum_product_three_values(values: list[int]) -> int:
    """Largest product of exactly three distinct indices; signed values, no mutation.

    At least three elements required; duplicates are separate indices.
    """
    if len(values) < 3: raise ValueError('at least three values required')
    initial = sorted(values[:3])
    low_a, low_b = initial[:2]
    high_a, high_b, high_c = initial[2], initial[1], initial[0]
    for i in range(3, len(values)):
        value = values[i]
        if value >= high_a: high_a, high_b, high_c = value, high_a, high_b
        elif value >= high_b: high_b, high_c = value, high_b
        elif value > high_c: high_c = value
        if value <= low_a: low_a, low_b = value, low_a
        elif value < low_b: low_b = value
    return max(high_a*high_b*high_c, high_a*low_a*low_b)
