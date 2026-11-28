def count_triplets_below_sum(values: list[int], target: int) -> int:
    """Count i<j<k with sum < target, retaining index multiplicities; no mutation."""
    ordered = sorted(values)
    answer = 0
    for first in range(len(ordered)-2):
        left, right = first+1, len(ordered)-1
        while left < right:
            if ordered[first]+ordered[left]+ordered[right] < target:
                answer += right-left
                left += 1
            else: right -= 1
    return answer
