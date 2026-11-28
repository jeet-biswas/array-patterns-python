def signed_radix_sort(values: list[int]) -> list[int]:
    """Return a fresh ascending integer sort using byte radix passes; no mutation."""
    if not values: return []
    offset = min(values)
    keys = [x-offset for x in values]
    shift = 0
    maximum = max(keys)
    while maximum >> shift:
        counts = [0]*256
        for key in keys: counts[(key >> shift) & 255] += 1
        start = 0
        for i, count in enumerate(counts):
            counts[i], start = start, start+count
        following = [0]*len(keys)
        for key in keys:
            digit = (key >> shift) & 255
            following[counts[digit]] = key
            counts[digit] += 1
        keys = following
        shift += 8
    return [key+offset for key in keys]
