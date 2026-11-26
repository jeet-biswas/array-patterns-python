def shortest_missing_roll_sequence(rolls: list[int], k: int) -> int:
    """Shortest sequence over faces 1..k absent as a subsequence of rolls.

    k must be positive and all rolls within 1..k. Input is unchanged.
    """
    if k <= 0 or any(not 1 <= x <= k for x in rolls):
        raise ValueError('positive k and valid faces required')
    seen = set()
    blocks = 0
    for value in rolls:
        seen.add(value)
        if len(seen) == k:
            blocks += 1
            seen.clear()
    return blocks+1
