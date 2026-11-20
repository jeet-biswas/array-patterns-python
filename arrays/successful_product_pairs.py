from bisect import bisect_left


def successful_product_pairs(first: list[int], second: list[int], threshold: int) -> list[int]:
    """For each first value, count second values whose product >= threshold.

    All inputs/threshold must be nonnegative, else ValueError. Multiplicity
    and first-array order are retained. O(m log m+n log(m+1)) time and
    O(n+m) space including output; inputs are unchanged.
    """
    if threshold < 0 or any(x < 0 for x in first) or any(x < 0 for x in second):
        raise ValueError('nonnegative values and threshold are required')
    if threshold == 0:
        return [len(second)] * len(first)
    ordered = sorted(second)
    result = []
    for value in first:
        if value == 0:
            result.append(0)
        else:
            needed = (threshold + value - 1) // value
            result.append(len(ordered) - bisect_left(ordered, needed))
    return result
