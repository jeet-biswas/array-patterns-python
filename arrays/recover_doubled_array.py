from collections import Counter


def recover_doubled_array(changed: list[int]) -> list[int] | None:
    """Return sorted original whose values plus doubles form changed, or None.

    Nonnegative values required; input is unchanged. Empty returns [].
    """
    if any(x < 0 for x in changed):
        raise ValueError('values must be nonnegative')
    if len(changed) % 2:
        return None
    counts = Counter(changed)
    original = []
    for value in sorted(changed):
        if counts[value] == 0:
            continue
        counts[value] -= 1
        if counts[2*value] == 0:
            return None
        counts[2*value] -= 1
        original.append(value)
    return original
