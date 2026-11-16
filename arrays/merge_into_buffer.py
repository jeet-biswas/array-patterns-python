def merge_into_buffer(destination: list[int], count: int, source: list[int]) -> None:
    """Merge sorted destination[:count] and source into destination in place.

    Requires len(destination) == count + len(source), valid count, and
    distinct input lists, else ValueError. Sortedness is unchecked.
    O(n+m) time, O(1) space; source is unchanged; returns None.
    """
    if (source is destination or not 0 <= count <= len(destination)
            or len(destination) != count + len(source)):
        raise ValueError('distinct lists and an exactly sized destination are required')
    left, right, write = count - 1, len(source) - 1, len(destination) - 1
    while right >= 0:
        if left >= 0 and destination[left] > source[right]:
            destination[write] = destination[left]
            left -= 1
        else:
            destination[write] = source[right]
            right -= 1
        write -= 1
