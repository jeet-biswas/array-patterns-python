from collections import Counter


def count_triplets_target_multiplicity(values: list[int], target: int) -> int:
    """Exact count of i<j<k summing to target; signed values allowed, no mutation."""
    counts = Counter(values)
    keys = sorted(counts)
    answer = 0
    for i, x in enumerate(keys):
        for j in range(i, len(keys)):
            y = keys[j]
            z = target-x-y
            if z < y: break
            if z not in counts: continue
            a, b, c = counts[x], counts[y], counts[z]
            if x == z: answer += a*(a-1)*(a-2)//6
            elif x == y: answer += a*(a-1)//2*c
            elif y == z: answer += a*b*(b-1)//2
            else: answer += a*b*c
    return answer
