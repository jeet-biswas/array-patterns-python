def minimum_job_schedule_difficulty(jobs: list[int], days: int) -> int | None:
    """Minimum sum of daily maxima for exactly days nonempty ordered blocks.

    Nonnegative jobs and days required. None means impossible; empty/zero days -> 0.
    Input is unchanged.
    """
    if days < 0 or any(x < 0 for x in jobs):
        raise ValueError('nonnegative days and difficulties required')
    if days == 0:
        return 0 if not jobs else None
    if days > len(jobs):
        return None
    previous = [None]*(len(jobs)+1)
    previous[0] = 0
    for day in range(1, days+1):
        current = [None]*(len(jobs)+1)
        for end in range(day, len(jobs)+1):
            maximum = 0
            for start in range(end-1, day-2, -1):
                maximum = max(maximum, jobs[start])
                if previous[start] is not None:
                    cost = previous[start]+maximum
                    current[end] = cost if current[end] is None else min(current[end], cost)
        previous = current
    return previous[-1]
