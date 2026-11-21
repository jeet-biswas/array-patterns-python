def longest_positive_product(values: list[int]) -> int:
    """Longest nonempty positive-product subarray length, or zero; no mutation."""
    positive = negative = best = 0
    for value in values:
        if value == 0:
            positive = negative = 0
        elif value > 0:
            positive += 1
            negative = negative + 1 if negative else 0
        else:
            positive, negative = (negative + 1 if negative else 0), positive + 1
        best = max(best, positive)
    return best
