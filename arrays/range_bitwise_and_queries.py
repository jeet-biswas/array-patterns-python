def range_bitwise_and_queries(values: list[int], queries: list[tuple[int, int]]) -> list[int]:
    """Answer AND over nonempty half-open [start,end) ranges; no mutation.

    Nonnegative values required; invalid or empty ranges raise IndexError.
    """
    if any(x < 0 for x in values): raise ValueError('nonnegative values required')
    table = [list(values)]
    size = 2
    while size <= len(values):
        previous = table[-1]
        half = size//2
        table.append([previous[i] & previous[i+half] for i in range(len(values)-size+1)])
        size *= 2
    result = []
    for start, end in queries:
        if not 0 <= start < end <= len(values): raise IndexError('nonempty valid range required')
        level = (end-start).bit_length()-1
        width = 1 << level
        result.append(table[level][start] & table[level][end-width])
    return result
