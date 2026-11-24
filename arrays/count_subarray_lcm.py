from math import lcm


def count_subarray_lcm(values: list[int], target: int) -> int:
    """Count nonempty subarrays with LCM exactly target; no mutation.

    Values and target must be positive integers.
    """
    if target <= 0 or any(x <= 0 for x in values):
        raise ValueError('positive values and target required')
    previous = {}
    total = 0
    for value in values:
        current = {}
        if target % value == 0:
            current[value] = 1
            for old, count in previous.items():
                combined = lcm(old, value)
                if target % combined == 0:
                    current[combined] = current.get(combined, 0)+count
        total += current.get(target, 0)
        previous = current
    return total
