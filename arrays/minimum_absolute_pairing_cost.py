def minimum_absolute_pairing_cost(first: list[int], second: list[int]) -> int:
    """Minimum sum of absolute differences across a one-to-one pairing; no mutation.

    Equal lengths required; signed values and duplicates allowed. Empty costs zero.
    """
    if len(first) != len(second):
        raise ValueError('equal lengths required')
    return sum(abs(a-b) for a, b in zip(sorted(first), sorted(second)))
