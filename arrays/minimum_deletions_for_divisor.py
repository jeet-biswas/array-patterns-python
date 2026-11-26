from math import gcd


def minimum_deletions_for_divisor(values: list[int], targets: list[int]) -> int | None:
    """Fewest deletions leaving a nonempty array whose minimum divides every target.

    Positive values and nonempty positive targets required. None if impossible;
    an empty values array is impossible. Inputs are unchanged.
    """
    if not targets or any(x <= 0 for x in targets) or any(x <= 0 for x in values):
        raise ValueError('positive values and nonempty positive targets required')
    common = 0
    for value in targets:
        common = gcd(common, value)
    for count, value in enumerate(sorted(values)):
        if common % value == 0:
            return count
    return None
