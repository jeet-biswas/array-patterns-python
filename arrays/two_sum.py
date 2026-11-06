def two_sum(values: list[int], target: int) -> tuple[int, int] | None:
    """Return a pair of distinct indices summing to target, or None.

    Chooses the earliest possible right index, then earliest matching left index.
    Does not modify values. Expected O(n) time and O(n) extra space.
    """
    seen = {}
    for right, value in enumerate(values):
        left = seen.get(target - value)
        if left is not None:
            return left, right
        seen.setdefault(value, right)
    return None
