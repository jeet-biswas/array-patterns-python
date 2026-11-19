from arrays.fenwick_range_sum import FenwickRangeSum


def offline_distinct_queries(values: list[int], queries: list[tuple[int, int]]) -> list[int]:
    """Distinct counts for half-open ranges in input query order; empty ranges -> 0.

    Malformed or invalid bounds raise ValueError. Expected
    O((n+q)*log(n+2)) time, O(n+q) space. Inputs are unchanged.
    """
    n = len(values)
    buckets = [[] for _ in range(n + 1)]
    for index, query in enumerate(queries):
        if len(query) != 2 or not 0 <= query[0] <= query[1] <= n:
            raise ValueError('queries must be valid half-open (start, stop) pairs')
        start, stop = query
        buckets[stop].append((start, index))
    tree = FenwickRangeSum([0] * n)
    latest = {}
    result = [0] * len(queries)
    for stop in range(n + 1):
        if stop:
            i, value = stop - 1, values[stop - 1]
            if value in latest:
                tree.add(latest[value], -1)
            tree.add(i, 1)
            latest[value] = i
        for start, index in buckets[stop]:
            result[index] = tree.query(start, stop)
    return result
