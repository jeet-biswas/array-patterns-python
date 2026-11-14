from collections import deque


def shortest_subarray_signed(values: list[int], target: int) -> int:
    """Shortest nonempty contiguous subarray with sum >= target; none -> 0.

    Any integer values and target are accepted. O(n) time and O(n) space.
    Input is unchanged; zero-length subarrays are never counted.
    """
    candidates = deque([(0, 0)])
    prefix = 0
    best = len(values) + 1
    for stop, value in enumerate(values, 1):
        prefix += value
        while candidates and prefix - candidates[0][1] >= target:
            start, _ = candidates.popleft()
            best = min(best, stop - start)
        while candidates and candidates[-1][1] >= prefix:
            candidates.pop()
        candidates.append((stop, prefix))
    return best if best <= len(values) else 0
