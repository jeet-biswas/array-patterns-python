def longest_majority_above_threshold(values: list[int], threshold: int) -> int:
    """Longest subarray where more than half the values exceed threshold; no mutation."""
    first = {0: -1}
    balance = best = 0
    for i, value in enumerate(values):
        balance += 1 if value > threshold else -1
        if balance > 0:
            best = i+1
        elif balance-1 in first:
            best = max(best, i-first[balance-1])
        first.setdefault(balance, i)
    return best
