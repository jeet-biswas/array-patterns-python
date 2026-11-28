def previous_permutation(values: list[int]) -> bool:
    """Rearrange to previous distinct lexicographic permutation; return whether it existed.

    At the smallest permutation, wrap to descending order and return False.
    Duplicates supported; empty and singleton return False.
    """
    pivot = len(values)-2
    while pivot >= 0 and values[pivot] <= values[pivot+1]: pivot -= 1
    found = pivot >= 0
    if found:
        other = len(values)-1
        while values[other] >= values[pivot]: other -= 1
        values[pivot], values[other] = values[other], values[pivot]
    left, right = pivot+1, len(values)-1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1
    return found
