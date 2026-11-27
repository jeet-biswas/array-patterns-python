def count_value_disjoint_partitions(values: list[int]) -> int:
    """Count partitions into nonempty contiguous blocks with no value in two blocks.

    Empty array has one empty partition. Exact integer result; no mutation.
    """
    last = {value: i for i, value in enumerate(values)}
    end = -1
    cuts = 0
    for i, value in enumerate(values):
        end = max(end, last[value])
        if i == end and i+1 < len(values):
            cuts += 1
    return 1 << cuts
