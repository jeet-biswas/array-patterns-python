def minimize_max_pair_difference(values: list[int], pairs: int) -> int:
    """Smallest largest absolute difference among exactly pairs disjoint index pairs.

    0 <= pairs <= len(values)//2 required; zero pairs returns zero. No mutation.
    """
    if not 0 <= pairs <= len(values)//2:
        raise ValueError('invalid pair count')
    if pairs == 0:
        return 0
    ordered = sorted(values)
    low, high = 0, ordered[-1]-ordered[0]
    while low < high:
        bound = (low+high)//2
        count = index = 0
        while index+1 < len(ordered):
            if ordered[index+1]-ordered[index] <= bound:
                count += 1
                index += 2
            else:
                index += 1
        if count >= pairs:
            high = bound
        else:
            low = bound+1
    return low
