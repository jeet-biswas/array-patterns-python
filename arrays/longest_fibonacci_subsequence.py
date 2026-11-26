def longest_fibonacci_subsequence(values: list[int]) -> int:
    """Longest Fibonacci-like subsequence length >= 3, or zero; no mutation.

    Values must be strictly increasing positive integers.
    """
    if any(x <= 0 for x in values) or any(values[i-1] >= values[i] for i in range(1, len(values))):
        raise ValueError('strictly increasing positive values required')
    positions = {value: i for i, value in enumerate(values)}
    lengths = {}
    best = 0
    for right in range(len(values)):
        for middle in range(right):
            left = positions.get(values[right]-values[middle])
            if left is not None and left < middle:
                length = lengths.get((left, middle), 2)+1
                lengths[middle, right] = length
                best = max(best, length)
    return best
