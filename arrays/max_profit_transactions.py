def max_profit_transactions(prices: list[int], limit: int) -> int:
    """Best profit from at most limit buy-then-sell transactions, one held share.

    Negative prices/limit raise ValueError. O(n*min(limit,n)) time and
    O(min(limit,n)) space; unlimited case O(n)/O(1). Input is unchanged.
    """
    if limit < 0 or any(price < 0 for price in prices):
        raise ValueError('prices and transaction limit must be nonnegative')
    if limit == 0 or len(prices) < 2:
        return 0
    if limit >= len(prices) // 2:
        return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))
    holding = [None] * limit
    sold = [0] * limit
    for price in prices:
        next_holding, next_sold = holding.copy(), sold.copy()
        for t in range(limit):
            buy = (sold[t-1] if t else 0) - price
            next_holding[t] = buy if holding[t] is None else max(holding[t], buy)
            if holding[t] is not None:
                next_sold[t] = max(sold[t], holding[t] + price)
        holding, sold = next_holding, next_sold
    return sold[-1]
