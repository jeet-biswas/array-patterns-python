def stable_counting_sort_records(records: list[tuple[int, int]], key_count: int) -> list[tuple[int, int]]:
    """Stable ascending sort of (key,payload) pairs; keys must be in 0..key_count-1.

    key_count must be nonnegative. Input is unchanged.
    """
    if key_count < 0 or any(not 0 <= key < key_count for key, _ in records):
        raise ValueError('keys outside supplied range')
    positions = [0]*key_count
    for key, _ in records: positions[key] += 1
    start = 0
    for key, count in enumerate(positions):
        positions[key], start = start, start+count
    result = [None]*len(records)
    for key, payload in records:
        result[positions[key]] = (key, payload)
        positions[key] += 1
    return result
