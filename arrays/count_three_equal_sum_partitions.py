def count_three_equal_sum_partitions(values: list[int]) -> int:
    """Count two cuts forming three nonempty contiguous equal-sum parts; no mutation."""
    total = sum(values)
    if len(values) < 3 or total % 3:
        return 0
    target = total//3
    prefix = first_count = answer = 0
    for i in range(len(values)-1):
        prefix += values[i]
        if prefix == 2*target:
            answer += first_count
        if prefix == target:
            first_count += 1
    return answer
