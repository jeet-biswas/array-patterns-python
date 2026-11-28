def heap_sort_in_place(values: list[int]) -> None:
    """Sort integers ascending in place; unstable, returns None."""
    def sift(root, end):
        while 2*root+1 < end:
            child = 2*root+1
            if child+1 < end and values[child+1] > values[child]: child += 1
            if values[root] >= values[child]: break
            values[root], values[child] = values[child], values[root]
            root = child
    for root in range(len(values)//2-1, -1, -1): sift(root, len(values))
    for end in range(len(values)-1, 0, -1):
        values[0], values[end] = values[end], values[0]
        sift(0, end)
