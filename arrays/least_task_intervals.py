from collections import Counter


def least_task_intervals(tasks: list[int], cooldown: int) -> int:
    """Fewest unit slots for reorderable task labels, with cooldown slots between equals.

    Idle slots allowed. cooldown must be nonnegative; input is unchanged.
    """
    if cooldown < 0:
        raise ValueError('cooldown must be nonnegative')
    if not tasks:
        return 0
    counts = Counter(tasks)
    frequency = max(counts.values())
    tied = sum(count == frequency for count in counts.values())
    return max(len(tasks), (frequency-1)*(cooldown+1)+tied)
