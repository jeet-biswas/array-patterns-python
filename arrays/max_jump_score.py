from collections import deque


def max_jump_score(values: list[int], k: int) -> int:
    """Best sum on a path from first to last index with jump lengths 1..k.

    Requires a nonempty array and positive k; input is unchanged.
    """
    if not values or k <= 0:
        raise ValueError('nonempty values and positive k required')
    dp = [values[0]]
    queue = deque([0])
    for i in range(1, len(values)):
        while queue[0] < i-k:
            queue.popleft()
        dp.append(values[i] + dp[queue[0]])
        while queue and dp[queue[-1]] <= dp[i]:
            queue.pop()
        queue.append(i)
    return dp[-1]
