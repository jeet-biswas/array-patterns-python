def max_subarray_one_deletion(values: list[int]) -> int:
    """Best sum from a contiguous segment after optionally deleting one element.

    At least one element must remain. Empty raises ValueError.
    O(n) time, O(1) space; input is unchanged.
    """
    if not values:
        raise ValueError('values must be nonempty')
    keep = best = values[0]
    deleted = None
    for i in range(1, len(values)):
        value = values[i]
        deleted = keep if deleted is None else max(keep, deleted + value)
        keep = max(value, keep + value)
        best = max(best, keep, deleted)
    return best
