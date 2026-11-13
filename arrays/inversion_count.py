def inversion_count(values: list[int]) -> int:
    """Count pairs i < j with values[i] > values[j]; equal values do not count.

    O(n log n) time, O(n) total auxiliary space. Input is not modified.
    """
    work = values.copy()
    buffer = [0] * len(values)

    def count(start, stop):
        if stop - start < 2:
            return 0
        middle = (start + stop) // 2
        total = count(start, middle) + count(middle, stop)
        left, right = start, middle
        for write in range(start, stop):
            if left < middle and (right == stop or work[left] <= work[right]):
                buffer[write] = work[left]
                left += 1
            else:
                buffer[write] = work[right]
                total += middle - left
                right += 1
        for i in range(start, stop):
            work[i] = buffer[i]
        return total

    return count(0, len(values))
