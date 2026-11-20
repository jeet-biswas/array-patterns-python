def max_profit_fee(prices: list[int], fee: int) -> int:
    """Best profit with unlimited sequential trades, charging fee on each sale.

    At most one held share. Negative prices/fee raise ValueError. Empty -> 0.
    O(n) time, O(1) space; input is unchanged.
    """
    if fee < 0 or any(price < 0 for price in prices):
        raise ValueError('prices and fee must be nonnegative')
    if not prices:
        return 0
    cash, holding = 0, -prices[0]
    for i in range(1, len(prices)):
        price = prices[i]
        cash, holding = max(cash, holding + price - fee), max(holding, cash - price)
    return cash
