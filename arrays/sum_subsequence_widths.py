def sum_subsequence_widths(values: list[int]) -> int:
    """Sum max-min over every nonempty index-distinct subsequence, no modulo.

    Empty -> 0; signed values allowed. O(n log n) comparisons and O(n)
    big-integer operations/slots. Powers may have O(n) bits. No mutation.
    """
    ordered = sorted(values)
    powers = [1]
    for _ in range(1, len(values)):
        powers.append(powers[-1] * 2)
    return sum(value * (powers[i] - powers[len(values)-1-i])
               for i, value in enumerate(ordered))
