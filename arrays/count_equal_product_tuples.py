def count_equal_product_tuples(values: list[int]) -> int:
    """Count ordered distinct indices (a,b,c,d) with values[a]*values[b]==values[c]*values[d].

    Values must be distinct positive integers. Input is unchanged.
    """
    if any(x <= 0 for x in values) or len(set(values)) != len(values):
        raise ValueError('distinct positive values required')
    products = {}
    total = 0
    for i, value in enumerate(values):
        for j in range(i):
            product = value*values[j]
            total += 8*products.get(product, 0)
            products[product] = products.get(product, 0)+1
    return total
