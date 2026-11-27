from bisect import bisect_left


def closest_subset_sum_difference(values: list[int], target: int) -> int:
    """Minimum absolute difference between target and a subset sum; no mutation.

    Signed values allowed, empty subset included. Exponential space/time: use
    moderate-size arrays.
    """
    def sums(start, end):
        result = [0]
        for i in range(start, end):
            result += [total+values[i] for total in result]
        return result
    middle = len(values)//2
    left = sums(0, middle)
    right = sorted(sums(middle, len(values)))
    best = abs(target)
    for value in left:
        at = bisect_left(right, target-value)
        for index in (at-1, at):
            if 0 <= index < len(right):
                best = min(best, abs(value+right[index]-target))
    return best
