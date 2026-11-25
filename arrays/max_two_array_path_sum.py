def max_two_array_path_sum(first: list[int], second: list[int]) -> int:
    """Maximum sum from the start of either sorted array to an end, switching at equals.

    Both arrays must be strictly increasing and nonnegative. A shared value is
    counted once per switch. Empty paths allowed; exact result, no mutation.
    """
    for values in (first, second):
        if any(x < 0 for x in values) or any(values[i-1] >= values[i] for i in range(1, len(values))):
            raise ValueError('strictly increasing nonnegative arrays required')
    i = j = total_a = total_b = 0
    while i < len(first) or j < len(second):
        if j == len(second) or i < len(first) and first[i] < second[j]:
            total_a += first[i]
            i += 1
        elif i == len(first) or second[j] < first[i]:
            total_b += second[j]
            j += 1
        else:
            total_a = total_b = max(total_a, total_b)+first[i]
            i += 1
            j += 1
    return max(total_a, total_b)
