def product_except_self(values: list[int]) -> list[int]:
    """Return each element's product excluding itself, without division.

    Empty -> []; singleton -> [1] (empty product).
    O(n) arithmetic operations; O(1) auxiliary space beyond O(n) output.
    """
    result = [1] * len(values)
    prefix = 1
    for i, value in enumerate(values):
        result[i] = prefix
        prefix *= value
    suffix = 1
    for i in range(len(values) - 1, -1, -1):
        result[i] *= suffix
        suffix *= values[i]
    return result
