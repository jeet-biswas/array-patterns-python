from bisect import bisect_left


def minimum_heater_radius(houses: list[int], heaters: list[int]) -> int | None:
    """Minimum common radius covering all houses; signed coordinates, no mutation.

    No houses -> 0. Houses with no heaters -> None. Duplicates allowed.
    """
    if not houses: return 0
    if not heaters: return None
    ordered = sorted(heaters)
    radius = 0
    for house in houses:
        at = bisect_left(ordered, house)
        distance = None
        for index in (at-1, at):
            if 0 <= index < len(ordered):
                candidate = abs(ordered[index]-house)
                distance = candidate if distance is None else min(distance, candidate)
        radius = max(radius, distance)
    return radius
