def minimum_squared_pair_difference(first: list[int], second: list[int], operations: int) -> int:
    """Minimize sum((first[i]-second[i])**2) using at most operations unit changes.

    A change adds/subtracts one to any element in either array. Equal lengths and
    nonnegative budget required; signed values supported. Inputs are unchanged.
    """
    if len(first) != len(second) or operations < 0: raise ValueError('invalid lengths or budget')
    differences = [abs(a-b) for a, b in zip(first, second)]
    if sum(differences) <= operations: return 0
    low, high = 0, max(differences)
    while low < high:
        level = (low+high)//2
        needed = sum(max(0, d-level) for d in differences)
        if needed <= operations: high = level
        else: low = level+1
    used = sum(max(0, d-low) for d in differences)
    total = sum(min(d, low)**2 for d in differences)
    return total-(operations-used)*(2*low-1)
