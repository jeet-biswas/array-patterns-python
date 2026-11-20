def count_subsequences_minmax(values: list[int], target: int) -> int:
    """Count nonempty index-distinct subsequences with min+max <= target.

    Counts are exact, without modulo. Signed values supported; no mutation.
    O(n log n) comparisons plus O(n) big-integer operations, O(n) integer
    slots. Counts and powers can have O(n) bits each.
    """
    ordered = sorted(values)
    powers = [1]
    for _ in range(1, len(values)):
        powers.append(powers[-1] * 2)
    left, right = 0, len(ordered) - 1
    total = 0
    while left <= right:
        if ordered[left] + ordered[right] <= target:
            total += powers[right-left]
            left += 1
        else:
            right -= 1
    return total
