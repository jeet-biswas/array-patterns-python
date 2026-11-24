import heapq


def furthest_reachable_building(heights: list[int], bricks: int, ladders: int) -> int:
    """Last reachable zero-based index; empty -> -1. No mutation.

    Upward moves cost their height difference in bricks or one ladder.
    Other moves are free. Heights and both budgets must be nonnegative.
    """
    if bricks < 0 or ladders < 0 or any(h < 0 for h in heights):
        raise ValueError('nonnegative heights and budgets required')
    climbs = []
    for i in range(len(heights)-1):
        rise = heights[i+1]-heights[i]
        if rise > 0:
            heapq.heappush(climbs, rise)
            if len(climbs) > ladders:
                bricks -= heapq.heappop(climbs)
                if bricks < 0:
                    return i
    return len(heights)-1
