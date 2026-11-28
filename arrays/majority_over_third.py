def majority_over_third(values: list[int]) -> list[int]:
    """Ascending values with count > len(values)/3; no mutation."""
    first = second = None
    count_a = count_b = 0
    for value in values:
        if value == first: count_a += 1
        elif value == second: count_b += 1
        elif count_a == 0: first, count_a = value, 1
        elif count_b == 0: second, count_b = value, 1
        else:
            count_a -= 1
            count_b -= 1
    return sorted(x for x in (first, second) if x is not None and values.count(x) > len(values)//3)
