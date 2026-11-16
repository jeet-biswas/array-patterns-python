def max_profit_cooldown(prices: list[int]) -> int:
    """Best profit with at most one held share and one day cooldown after a sale.

    Nonnegative integer prices required (ValueError otherwise). Empty -> 0.
    O(n) time, O(1) space; input is unchanged.
    """
    if any(price < 0 for price in prices):
        raise ValueError('prices must be nonnegative')
    if not prices:
        return 0
    holding = -prices[0]
    sold = None
    resting = 0
    for i in range(1, len(prices)):
        price = prices[i]
        holding, sold, resting = (
            max(holding, resting - price),
            holding + price,
            resting if sold is None else max(resting, sold),
        )
    return resting if sold is None else max(resting, sold)
