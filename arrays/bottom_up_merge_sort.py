def bottom_up_merge_sort(values: list[int]) -> list[int]:
    """Return a fresh ascending stable sort using iterative merge sort; no mutation."""
    source = list(values)
    destination = [0]*len(values)
    width = 1
    while width < len(values):
        for start in range(0, len(values), 2*width):
            middle, end = min(start+width, len(values)), min(start+2*width, len(values))
            left, right = start, middle
            for out in range(start, end):
                if right == end or left < middle and source[left] <= source[right]:
                    destination[out] = source[left]
                    left += 1
                else:
                    destination[out] = source[right]
                    right += 1
        source, destination = destination, source
        width *= 2
    return source
