def find_duplicate_cycle(values: list[int]) -> int:
    """Find the unique repeated value in n+1 entries from 1..n; no mutation.

    Exactly one distinct value must repeat (unchecked); it may appear more than
    twice. Length/domain violations raise ValueError.
    """
    n = len(values)-1
    if n < 1 or any(not 1 <= x <= n for x in values): raise ValueError('invalid domain')
    slow, fast = values[0], values[values[0]]
    while slow != fast:
        slow, fast = values[slow], values[values[fast]]
    entrance = 0
    while entrance != slow:
        entrance, slow = values[entrance], values[slow]
    return entrance
