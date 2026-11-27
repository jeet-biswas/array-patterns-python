def max_worker_assignment_profit(difficulty: list[int], profit: list[int], workers: list[int]) -> int:
    """Assign each worker at most one reusable job within ability; return total profit.

    Job arrays need equal lengths; all quantities must be nonnegative. No mutation.
    """
    if len(difficulty) != len(profit) or any(x < 0 for a in (difficulty, profit, workers) for x in a):
        raise ValueError('equal job lengths and nonnegative values required')
    jobs = sorted(zip(difficulty, profit))
    at = best = total = 0
    for ability in sorted(workers):
        while at < len(jobs) and jobs[at][0] <= ability:
            best = max(best, jobs[at][1])
            at += 1
        total += best
    return total
