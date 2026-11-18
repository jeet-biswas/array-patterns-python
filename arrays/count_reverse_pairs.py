def count_reverse_pairs(values: list[int]) -> int:
    """Count index pairs i < j with values[i] > 2*values[j].

    Signed integers supported. O(n log n) time, O(n) space; input unchanged.
    """
    work = values.copy()
    buffer = [0] * len(values)

    def count(start, stop):
        if stop - start < 2:
            return 0
        middle = (start + stop) // 2
        total = count(start, middle) + count(middle, stop)
        right = middle
        for left in range(start, middle):
            while right < stop and work[left] > 2 * work[right]:
                right += 1
            total += right - middle
        left, right = start, middle
        for write in range(start, stop):
            if left < middle and (right == stop or work[left] <= work[right]):
                buffer[write] = work[left]
                left += 1
            else:
                buffer[write] = work[right]
                right += 1
        for i in range(start, stop):
            work[i] = buffer[i]
        return total

    return count(0, len(values))
