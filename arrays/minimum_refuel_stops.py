import heapq


def minimum_refuel_stops(target: int, fuel: int, stations: list[tuple[int, int]]) -> int:
    """Fewest stops to reach target, or -1; one fuel unit covers one distance unit.

    Stations (position, fuel) must be sorted by position; all quantities nonnegative.
    Tank is unbounded, fuel can reach exactly zero at a station. No mutation.
    """
    if target < 0 or fuel < 0 or any(p < 0 or amount < 0 for p, amount in stations):
        raise ValueError('nonnegative quantities required')
    if any(stations[i-1][0] > stations[i][0] for i in range(1, len(stations))):
        raise ValueError('stations must be sorted')
    available = []
    index = stops = 0
    reach = fuel
    while reach < target:
        while index < len(stations) and stations[index][0] <= reach:
            heapq.heappush(available, -stations[index][1])
            index += 1
        if not available:
            return -1
        reach -= heapq.heappop(available)
        stops += 1
    return stops
