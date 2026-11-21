def only_local_inversions(values: list[int]) -> bool:
    """True if every pair i<j with values[i]>values[j] has j=i+1; no mutation."""
    if len(values) < 3:
        return True
    earlier_max = values[0]
    for i in range(2, len(values)):
        earlier_max = max(earlier_max, values[i-2])
        if earlier_max > values[i]:
            return False
    return True
