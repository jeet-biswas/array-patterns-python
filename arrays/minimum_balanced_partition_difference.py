from bisect import bisect_left


def minimum_balanced_partition_difference(values: list[int]) -> int:
    """Minimum absolute sum difference between two equally sized index groups.

    Even length required, signed integers allowed. Empty -> 0; no mutation.
    Exponential algorithm intended for moderate-size arrays.
    """
    if len(values) % 2:
        raise ValueError('even length required')
    half = len(values)//2
    def grouped(start):
        result = [[] for _ in range(half+1)]
        result[0] = [0]
        for used in range(1, half+1):
            value = values[start+used-1]
            for count in range(used, 0, -1):
                result[count].extend(total+value for total in result[count-1])
        return result
    left, right = grouped(0), grouped(half)
    for group in right: group.sort()
    total = sum(values)
    best = None
    for count, group in enumerate(left):
        complements = right[half-count]
        for value in group:
            at = bisect_left(complements, (total-2*value+1)//2)
            for index in (at-1, at):
                if 0 <= index < len(complements):
                    cost = abs(total-2*(value+complements[index]))
                    best = cost if best is None else min(best, cost)
    return best
