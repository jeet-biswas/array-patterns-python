def triangle_count(lengths: list[int]) -> int:
    """Count index-distinct triplets forming a nondegenerate triangle.

    Nonnegative lengths required (ValueError otherwise); zeros cannot form
    a triangle. O(n squared) time, O(n) space; input is unchanged.
    """
    if any(length < 0 for length in lengths):
        raise ValueError('lengths must be nonnegative')
    ordered = sorted(lengths)
    total = 0
    for largest in range(2, len(ordered)):
        left, right = 0, largest - 1
        while left < right:
            if ordered[left] + ordered[right] > ordered[largest]:
                total += right - left
                right -= 1
            else:
                left += 1
    return total
