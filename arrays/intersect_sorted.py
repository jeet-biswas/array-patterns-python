def intersect_sorted(left: list[int], right: list[int]) -> list[int]:
    """Sorted multiset intersection; inputs must be nondecreasing (unchecked).

    O(n+m) time; O(1) auxiliary space apart from output. Does not mutate inputs.
    """
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            i += 1
        elif left[i] > right[j]:
            j += 1
        else:
            result.append(left[i])
            i += 1
            j += 1
    return result
