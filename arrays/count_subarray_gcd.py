from math import gcd


def count_subarray_gcd(values: list[int], target: int) -> int:
    """Count nonempty subarrays with GCD exactly target; no mutation.

    All values and target must be positive integers.
    """
    if target <= 0 or any(x <= 0 for x in values):
        raise ValueError('positive values and target required')
    previous = {}
    total = 0
    for value in values:
        current = {value: 1}
        for old, count in previous.items():
            combined = gcd(old, value)
            current[combined] = current.get(combined, 0)+count
        total += current.get(target, 0)
        previous = current
    return total
