from collections import Counter


def minimum_equal_group_removals(values: list[int]) -> int | None:
    """Remove any two or three equal values per operation; minimum count or None.

    Equal values need not be adjacent. Empty -> 0; input is unchanged.
    """
    total = 0
    for count in Counter(values).values():
        if count == 1:
            return None
        total += (count+2)//3
    return total
