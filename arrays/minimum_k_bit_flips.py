def minimum_k_bit_flips(values: list[int], k: int) -> int:
    """Minimum flips of exactly k consecutive bits to make all ones, or -1.

    k must be positive and values binary. Empty needs zero flips; no mutation.
    """
    if k <= 0 or any(x not in (0, 1) for x in values):
        raise ValueError('positive k and binary values required')
    expires = [0] * (len(values)+1)
    parity = total = 0
    for i, value in enumerate(values):
        parity ^= expires[i]
        if value ^ parity == 0:
            if i+k > len(values):
                return -1
            parity ^= 1
            expires[i+k] ^= 1
            total += 1
    return total
