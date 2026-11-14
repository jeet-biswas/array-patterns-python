def four_sum(values: list[int], target: int) -> list[tuple[int, int, int, int]]:
    """Unique value quadruplets summing to target, using four distinct indices.

    Input is unchanged. O(n cubed) time; O(n) sorting space plus output.
    """
    ordered = sorted(values)
    result = []
    n = len(ordered)
    for i in range(n - 3):
        if i and ordered[i] == ordered[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and ordered[j] == ordered[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = ordered[i] + ordered[j] + ordered[left] + ordered[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    result.append((ordered[i], ordered[j], ordered[left], ordered[right]))
                    low, high = ordered[left], ordered[right]
                    while left < right and ordered[left] == low:
                        left += 1
                    while left < right and ordered[right] == high:
                        right -= 1
    return result
