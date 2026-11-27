def count_subarrays_median_value(values: list[int], target: int) -> int:
    """Count nonempty subarrays with lower median target; distinct values required.

    Lower median means sorted_window[(length-1)//2]. Missing target -> 0; no mutation.
    """
    if len(set(values)) != len(values):
        raise ValueError('distinct values required')
    if target not in values:
        return 0
    pivot = values.index(target)
    counts = {0: 1}
    balance = 0
    for i in range(pivot-1, -1, -1):
        balance += 1 if values[i] > target else -1
        counts[balance] = counts.get(balance, 0)+1
    answer = counts.get(0, 0)+counts.get(1, 0)
    balance = 0
    for i in range(pivot+1, len(values)):
        balance += 1 if values[i] > target else -1
        answer += counts.get(-balance, 0)+counts.get(1-balance, 0)
    return answer
