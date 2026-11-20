def min_bouquet_day(bloom_days: list[int], bouquets: int, size: int) -> int:
    """Earliest day to form bouquets disjoint adjacent groups of size flowers.

    Nonnegative days/bouquets and positive size required, else ValueError.
    Zero bouquets -> 0; insufficient flowers -> -1. O(n log(D+1)) time
    for maximum day D, O(1) space; input is unchanged.
    """
    if bouquets < 0 or size <= 0 or any(day < 0 for day in bloom_days):
        raise ValueError('valid nonnegative days/count and positive size are required')
    if bouquets == 0:
        return 0
    if bouquets * size > len(bloom_days):
        return -1
    low, high = min(bloom_days), max(bloom_days)
    while low < high:
        day = (low + high) // 2
        run = made = 0
        for bloom in bloom_days:
            if bloom <= day:
                run += 1
                if run == size:
                    made += 1
                    run = 0
            else:
                run = 0
        if made >= bouquets:
            high = day
        else:
            low = day + 1
    return low
