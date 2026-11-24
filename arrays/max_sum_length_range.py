from collections import deque


def max_sum_length_range(values: list[int], minimum: int, maximum: int) -> int | None:
    """Best nonempty subarray sum with minimum <= length <= maximum, or None.

    Requires 1 <= minimum <= maximum. Signed values allowed; no mutation.
    """
    if not 1 <= minimum <= maximum:
        raise ValueError('invalid length range')
    prefix = [0]
    for x in values:
        prefix.append(prefix[-1]+x)
    queue = deque()
    best = None
    for end in range(minimum, len(values)+1):
        start = end-minimum
        while queue and prefix[queue[-1]] >= prefix[start]:
            queue.pop()
        queue.append(start)
        while queue[0] < end-maximum:
            queue.popleft()
        candidate = prefix[end]-prefix[queue[0]]
        best = candidate if best is None else max(best, candidate)
    return best
