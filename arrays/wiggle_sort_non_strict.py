def wiggle_sort_non_strict(values: list[int]) -> None:
    """Rearrange in place so a[0] <= a[1] >= a[2] <= a[3] ...; returns None."""
    for i in range(1, len(values)):
        if (i % 2 and values[i-1] > values[i]) or (i % 2 == 0 and values[i-1] < values[i]):
            values[i-1], values[i] = values[i], values[i-1]
