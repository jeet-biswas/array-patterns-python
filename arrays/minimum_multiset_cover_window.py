from collections import Counter


def minimum_multiset_cover_window(values: list[int], required: list[int]) -> tuple[int, int] | None:
    """Shortest [start,end) containing every required copy, or None; no mutation.

    Ties use earliest start; empty requirement returns (0,0).
    """
    if not required: return (0, 0)
    need = Counter(required)
    missing = len(required)
    left = 0
    best = None
    for right, value in enumerate(values):
        if value in need:
            missing -= need[value] > 0
            need[value] -= 1
        while missing == 0:
            if best is None or right+1-left < best[1]-best[0]: best = (left, right+1)
            removed = values[left]
            if removed in need:
                need[removed] += 1
                missing += need[removed] > 0
            left += 1
    return best
