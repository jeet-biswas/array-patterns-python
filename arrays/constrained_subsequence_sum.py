from collections import deque


def constrained_subsequence_sum(values: list[int], k: int) -> int:
    """Maximum nonempty subsequence sum with consecutive index gaps <= k.

    Nonempty input and positive k required; input is unchanged.
    """
    if not values or k <= 0:
        raise ValueError('nonempty values and positive k required')
    queue = deque()
    best = values[0]
    for i, value in enumerate(values):
        while queue and queue[0][0] < i-k:
            queue.popleft()
        score = value + (max(0, queue[0][1]) if queue else 0)
        best = max(best, score)
        while queue and queue[-1][1] <= score:
            queue.pop()
        queue.append((i, score))
    return best
