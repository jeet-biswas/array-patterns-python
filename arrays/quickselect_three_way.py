def quickselect_three_way(values: list[int], k: int) -> int:
    """Return the one-based kth smallest value; rearranges input in place.

    Duplicate values count separately. Invalid rank raises ValueError before mutation.
    """
    if not 1 <= k <= len(values): raise ValueError('rank out of range')
    target = k-1
    left, right = 0, len(values)-1
    while True:
        pivot = values[(left+right)//2]
        lower = index = left
        upper = right
        while index <= upper:
            if values[index] < pivot:
                values[lower], values[index] = values[index], values[lower]
                lower += 1
                index += 1
            elif values[index] > pivot:
                values[index], values[upper] = values[upper], values[index]
                upper -= 1
            else: index += 1
        if target < lower: right = lower-1
        elif target > upper: left = upper+1
        else: return pivot
