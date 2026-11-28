def shortest_subsequence_window(values: list[int], pattern: list[int]) -> tuple[int, int] | None:
    """Shortest [start,end) containing pattern as a subsequence, or None; no mutation.

    Ties use earliest start. Empty pattern returns (0,0).
    """
    if not pattern: return (0, 0)
    starts = [None]*len(pattern)
    best = None
    for i, value in enumerate(values):
        for j in range(len(pattern)-1, -1, -1):
            if value == pattern[j]:
                if j == 0: starts[j] = i
                elif starts[j-1] is not None: starts[j] = starts[j-1]
        if value == pattern[-1] and starts[-1] is not None:
            candidate = (starts[-1], i+1)
            if best is None or candidate[1]-candidate[0] < best[1]-best[0]: best = candidate
    return best
