def gas_station_start(gas: list[int], cost: list[int]) -> int:
    """Any feasible start for one clockwise circuit with initially empty tank.

    At station i, collect gas[i], then spend cost[i] to reach the next.
    Unlimited tank capacity. Empty or impossible -> -1. Unequal lengths
    or negative entries raise ValueError. O(n) time, O(1) space; no mutation.
    """
    if len(gas) != len(cost) or any(x < 0 for x in gas) or any(x < 0 for x in cost):
        raise ValueError('equal-length nonnegative arrays are required')
    if not gas:
        return -1
    total = tank = start = 0
    for i in range(len(gas)):
        difference = gas[i] - cost[i]
        total += difference
        tank += difference
        if tank < 0:
            start = i + 1
            tank = 0
    return start if total >= 0 else -1
