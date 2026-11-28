def count_subarrays_and_value(values: list[int], target: int) -> int:
    """Count nonempty subarrays whose bitwise AND equals target; no mutation.

    Nonnegative array values and target required.
    """
    if target < 0 or any(x < 0 for x in values): raise ValueError('nonnegative inputs required')
    previous = {}
    answer = 0
    for value in values:
        current = {value: 1}
        for old, count in previous.items():
            combined = old & value
            current[combined] = current.get(combined, 0)+count
        answer += current.get(target, 0)
        previous = current
    return answer
