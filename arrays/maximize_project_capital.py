import heapq


def maximize_project_capital(required: list[int], profits: list[int], k: int, capital: int) -> int:
    """Maximum final capital after at most k projects, each usable once; no mutation.

    Equal-length arrays and nonnegative requirements, profits, k and capital required.
    Choosing a project adds its profit without subtracting its requirement.
    """
    if len(required) != len(profits) or k < 0 or capital < 0:
        raise ValueError('invalid lengths or budget')
    if any(x < 0 for x in required) or any(x < 0 for x in profits):
        raise ValueError('nonnegative requirements and profits required')
    projects = sorted(zip(required, profits))
    available = []
    index = 0
    for _ in range(min(k, len(projects))):
        while index < len(projects) and projects[index][0] <= capital:
            heapq.heappush(available, -projects[index][1])
            index += 1
        if not available:
            break
        capital -= heapq.heappop(available)
    return capital
