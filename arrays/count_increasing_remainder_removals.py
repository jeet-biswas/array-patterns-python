def count_increasing_remainder_removals(values: list[int]) -> int:
    """Count nonempty contiguous removals leaving a strictly increasing remainder.

    Empty/singleton remainders qualify; an empty input has no removals. No mutation.
    """
    n = len(values)
    if n == 0:
        return 0
    prefix_end = 0
    while prefix_end+1 < n and values[prefix_end] < values[prefix_end+1]:
        prefix_end += 1
    if prefix_end == n-1:
        return n*(n+1)//2
    total = prefix_end+2
    for suffix_start in range(n-1, 0, -1):
        if suffix_start < n-1 and values[suffix_start] >= values[suffix_start+1]:
            break
        while prefix_end >= 0 and values[prefix_end] >= values[suffix_start]:
            prefix_end -= 1
        total += prefix_end+2
    return total
