def equal_value_index_distances(values: list[int]) -> list[int]:
    """At each index i return sum(abs(i-j)) over all j with equal values; no mutation."""
    counts, totals = {}, {}
    for i, value in enumerate(values):
        counts[value] = counts.get(value, 0)+1
        totals[value] = totals.get(value, 0)+i
    seen_counts, seen_totals = {}, {}
    result = []
    for i, value in enumerate(values):
        count = seen_counts.get(value, 0)
        total = seen_totals.get(value, 0)
        left = i*count-total
        right = totals[value]-total-i-i*(counts[value]-count-1)
        result.append(left+right)
        seen_counts[value] = count+1
        seen_totals[value] = total+i
    return result
