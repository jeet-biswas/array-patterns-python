def max_stock_profit(prices: list[int]) -> int:
    """Best profit from at most one buy followed by one sell; empty -> 0.

    Negative prices raise ValueError. O(n) time and O(1) extra space.
    """
    if any(price < 0 for price in prices):
        raise ValueError('prices must be nonnegative')
    if not prices:
        return 0
    minimum = prices[0]
    best = 0
    for i in range(1, len(prices)):
        best = max(best, prices[i] - minimum)
        minimum = min(minimum, prices[i])
    return best
