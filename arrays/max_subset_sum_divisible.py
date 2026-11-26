def max_subset_sum_divisible(values: list[int], modulus: int) -> int:
    """Maximum subset sum divisible by positive modulus, allowing empty; no mutation.

    Values may be signed. Each index may be selected once.
    """
    if modulus <= 0:
        raise ValueError('positive modulus required')
    best = [None]*modulus
    best[0] = 0
    for value in values:
        following = best.copy()
        for total in best:
            if total is not None:
                candidate = total+value
                remainder = candidate % modulus
                if following[remainder] is None or candidate > following[remainder]:
                    following[remainder] = candidate
        best = following
    return best[0]
