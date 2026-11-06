def merge_sorted(left: list[int], right: list[int]) -> list[int]:
    """Return a merged array; inputs must be sorted (not checked).

    O(n + m) time and output space, O(1) auxiliary space excluding output.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
