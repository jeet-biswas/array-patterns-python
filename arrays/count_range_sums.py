def count_range_sums(values: list[int], lower: int, upper: int) -> int:
    """Count nonempty contiguous subarrays with lower <= sum <= upper.

    Reversed bounds raise ValueError. O(n log n) time, O(n) space; no mutation.
    """
    if lower > upper:
        raise ValueError('lower must not exceed upper')
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)
    buffer = [0] * len(prefix)

    def count(start, stop):
        if stop - start < 2:
            return 0
        middle = (start + stop) // 2
        total = count(start, middle) + count(middle, stop)
        low = high = middle
        for left in range(start, middle):
            while low < stop and prefix[low] - prefix[left] < lower:
                low += 1
            while high < stop and prefix[high] - prefix[left] <= upper:
                high += 1
            total += high - low
        left, right = start, middle
        for write in range(start, stop):
            if left < middle and (right == stop or prefix[left] <= prefix[right]):
                buffer[write] = prefix[left]
                left += 1
            else:
                buffer[write] = prefix[right]
                right += 1
        for i in range(start, stop):
            prefix[i] = buffer[i]
        return total

    return count(0, len(prefix))
