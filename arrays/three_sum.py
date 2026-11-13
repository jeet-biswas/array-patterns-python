def three_sum(values: list[int]) -> list[tuple[int, int, int]]:
    """Unique sorted value triplets summing to zero, using distinct indices.

    Does not modify values. O(n squared) time and O(n) auxiliary space
    for sorting, excluding potentially O(n squared) output.
    """
    ordered = sorted(values)
    result = []
    for i in range(len(ordered) - 2):
        if i and ordered[i] == ordered[i - 1]:
            continue
        left, right = i + 1, len(ordered) - 1
        while left < right:
            total = ordered[i] + ordered[left] + ordered[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append((ordered[i], ordered[left], ordered[right]))
                low, high = ordered[left], ordered[right]
                while left < right and ordered[left] == low:
                    left += 1
                while left < right and ordered[right] == high:
                    right -= 1
    return result
