def final_discount_prices(prices: list[int]) -> list[int]:
    """Subtract the first later price <= each original price, if one exists.

    Nonnegative prices required (ValueError otherwise). O(n) time,
    O(n) space including output; input is unchanged.
    """
    if any(price < 0 for price in prices):
        raise ValueError('prices must be nonnegative')
    result = prices.copy()
    waiting = []
    for i, price in enumerate(prices):
        while waiting and prices[waiting[-1]] >= price:
            result[waiting.pop()] -= price
        waiting.append(i)
    return result
