def has_valid_block_partition(values: list[int]) -> bool:
    """Partition into equal pairs, equal triples, or triples x,x+1,x+2.

    Empty has a valid empty partition. Signed values allowed; no mutation.
    """
    valid = [False]*(len(values)+1)
    valid[0] = True
    for end in range(2, len(values)+1):
        if valid[end-2] and values[end-2] == values[end-1]:
            valid[end] = True
        if end >= 3 and valid[end-3]:
            a, b, c = values[end-3:end]
            valid[end] |= a == b == c or a+1 == b and b+1 == c
    return valid[-1]
