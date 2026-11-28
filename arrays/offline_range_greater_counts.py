def offline_range_greater_counts(values: list[int], queries: list[tuple[int, int, int]]) -> list[int]:
    """For (start,end,threshold), count values > threshold in [start,end); no mutation."""
    n = len(values)
    for start, end, _ in queries:
        if not 0 <= start <= end <= n: raise IndexError('invalid range')
    elements = sorted(((value, i) for i, value in enumerate(values)), reverse=True)
    ordered = sorted(((threshold, start, end, i) for i, (start, end, threshold) in enumerate(queries)), reverse=True)
    tree = [0]*(n+1)
    def prefix(end):
        total = 0
        while end:
            total += tree[end]
            end -= end & -end
        return total
    answers = [0]*len(queries)
    at = 0
    for threshold, start, end, query_id in ordered:
        while at < n and elements[at][0] > threshold:
            index = elements[at][1]+1
            while index <= n:
                tree[index] += 1
                index += index & -index
            at += 1
        answers[query_id] = prefix(end)-prefix(start)
    return answers
