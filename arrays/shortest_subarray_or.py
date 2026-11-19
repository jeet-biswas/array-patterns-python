def shortest_subarray_or(values: list[int], target: int) -> int:
    """Shortest nonempty contiguous window with bitwise OR >= positive target.

    None found -> 0. Negative values or target <= 0 raise ValueError.
    O(nB) bit-update steps, O(B) space for maximum input bit length B.
    Input unchanged; big-integer costs depend on B.
    """
    if target <= 0 or any(value < 0 for value in values):
        raise ValueError('nonnegative values and positive target are required')
    width = max(1, max(values, default=0).bit_length())
    counts = [0] * width
    left = current = 0
    best = len(values) + 1
    for right, value in enumerate(values):
        for bit in range(width):
            if value & (1 << bit):
                counts[bit] += 1
                current |= 1 << bit
        while current >= target and left <= right:
            best = min(best, right - left + 1)
            for bit in range(width):
                if values[left] & (1 << bit):
                    counts[bit] -= 1
                    if counts[bit] == 0:
                        current &= ~(1 << bit)
            left += 1
    return best if best <= len(values) else 0
