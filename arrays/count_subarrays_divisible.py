def count_subarrays_divisible(values: list[int], k: int) -> int:
    """Count nonempty contiguous subarrays whose sum is divisible by positive k.

    k <= 0 raises ValueError. Expected O(n) time and O(min(n,k)) space
    (plus the initial remainder entry); input is unchanged.
    """
    if k <= 0:
        raise ValueError('k must be positive')
    frequencies = {0: 1}
    remainder = total = 0
    for value in values:
        remainder = (remainder + value) % k
        total += frequencies.get(remainder, 0)
        frequencies[remainder] = frequencies.get(remainder, 0) + 1
    return total
