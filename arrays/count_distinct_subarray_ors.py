def count_distinct_subarray_ors(values: list[int]) -> int:
    """Number of different OR results among nonempty contiguous subarrays.

    Negative values raise ValueError; empty -> 0. Expected O(nB) set
    operations and O(nB) space for max bit width B (at least one).
    Integer hashing/bit-operation costs depend on B. Input is unchanged.
    """
    if any(value < 0 for value in values):
        raise ValueError('values must be nonnegative')
    ending = set()
    seen = set()
    for value in values:
        ending = {value} | {previous | value for previous in ending}
        seen.update(ending)
    return len(seen)
