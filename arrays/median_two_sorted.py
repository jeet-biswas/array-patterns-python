def median_two_sorted(left: list[int], right: list[int]) -> float:
    """Median of two nondecreasing arrays (sortedness unchecked); no mutation.

    Both empty raises ValueError. O(log(min(n,m)+1)) time, O(1) space.
    Returns a float; inputs should have magnitudes representable as floats.
    """
    if not left and not right:
        raise ValueError('at least one value is required')
    if len(left) > len(right):
        left, right = right, left
    n, m = len(left), len(right)
    low, high = 0, n
    half = (n + m + 1) // 2
    while low <= high:
        i = (low + high) // 2
        j = half - i
        a = left[i - 1] if i else float('-inf')
        b = left[i] if i < n else float('inf')
        c = right[j - 1] if j else float('-inf')
        d = right[j] if j < m else float('inf')
        if a <= d and c <= b:
            if (n + m) % 2:
                return float(max(a, c))
            return (max(a, c) + min(b, d)) / 2
        if a > d:
            high = i - 1
        else:
            low = i + 1
    raise ValueError('inputs must be sorted')
