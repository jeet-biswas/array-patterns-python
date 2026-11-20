def min_total_trip_time(times: list[int], trips: int) -> int:
    """Earliest integer time for at least trips completions by parallel workers.

    Worker times must be positive and trips nonnegative, else ValueError.
    No workers with positive trips raises ValueError; zero trips -> 0.
    O(n log(T+1)) time for T=min(times)*trips, O(1) space; no mutation.
    """
    if trips < 0 or any(time <= 0 for time in times):
        raise ValueError('positive worker times and nonnegative trips are required')
    if trips == 0:
        return 0
    if not times:
        raise ValueError('positive trips require a worker')
    low, high = 0, min(times) * trips
    while low < high:
        middle = (low + high) // 2
        if sum(middle // time for time in times) >= trips:
            high = middle
        else:
            low = middle + 1
    return low
