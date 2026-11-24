from collections import Counter


def can_pair_divisible_sums(values: list[int], modulus: int) -> bool:
    """Whether all elements can be paired with sums divisible by positive modulus.

    Signed values allowed; empty is valid. Input is unchanged.
    """
    if modulus <= 0:
        raise ValueError('positive modulus required')
    if len(values) % 2:
        return False
    counts = Counter(x % modulus for x in values)
    for remainder, count in counts.items():
        other = (-remainder) % modulus
        if other == remainder:
            if count % 2:
                return False
        elif counts[other] != count:
            return False
    return True
