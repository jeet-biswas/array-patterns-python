def max_time_weighted_satisfaction(values: list[int]) -> int:
    """Select and reorder any values to maximize sum((i+1)*value[i]).

    Empty selection is allowed. Signed inputs supported; no mutation.
    """
    suffix = total = 0
    for value in sorted(values, reverse=True):
        suffix += value
        if suffix <= 0:
            break
        total += suffix
    return total
