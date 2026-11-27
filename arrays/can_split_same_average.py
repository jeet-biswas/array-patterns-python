def can_split_same_average(values: list[int]) -> bool:
    """Whether indices can split into two nonempty groups with equal exact averages.

    Signed integers supported; input is unchanged. Uses exact integer arithmetic.
    """
    n = len(values)
    if n < 2:
        return False
    total = sum(values)
    sizes = [k for k in range(1, n//2+1) if total*k % n == 0]
    if not sizes:
        return False
    maximum = max(sizes)
    reachable = [set() for _ in range(maximum+1)]
    reachable[0].add(0)
    for used, value in enumerate(values, 1):
        for size in range(min(used, maximum), 0, -1):
            reachable[size].update(s+value for s in reachable[size-1])
    return any(total*k//n in reachable[k] for k in sizes)
