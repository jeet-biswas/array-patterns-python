def max_subsequence_dot_product(first: list[int], second: list[int]) -> int:
    """Maximum dot product of equal-length nonempty subsequences; no mutation.

    Both inputs must be nonempty. Order is preserved within each input.
    """
    if not first or not second:
        raise ValueError('both arrays must be nonempty')
    previous = [None] * (len(second)+1)
    for x in first:
        current = [None] * (len(second)+1)
        for j, y in enumerate(second, 1):
            product = x*y
            choices = [product]
            if previous[j-1] is not None:
                choices.append(product + previous[j-1])
            if previous[j] is not None:
                choices.append(previous[j])
            if current[j-1] is not None:
                choices.append(current[j-1])
            current[j] = max(choices)
        previous = current
    return previous[-1]
