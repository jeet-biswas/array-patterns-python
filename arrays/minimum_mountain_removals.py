from bisect import bisect_left


def minimum_mountain_removals(values: list[int]) -> int | None:
    """Minimum deletions leaving a strict rise then strict fall, both nonempty.

    At least three retained values are required. None means impossible; no mutation.
    """
    def lengths(sequence):
        tails, result = [], []
        for value in sequence:
            at = bisect_left(tails, value)
            if at == len(tails):
                tails.append(value)
            else:
                tails[at] = value
            result.append(at+1)
        return result
    up = lengths(values)
    down = lengths(reversed(values))[::-1]
    longest = max((a+b-1 for a, b in zip(up, down) if a > 1 and b > 1), default=0)
    return len(values)-longest if longest else None
