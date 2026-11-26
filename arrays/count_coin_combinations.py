def count_coin_combinations(coins: list[int], target: int) -> int:
    """Exact unordered combination count using unlimited coins; duplicates ignored.

    Positive denominations and nonnegative target required; no mutation.
    Empty combination is the single way to make zero.
    """
    if target < 0 or any(x <= 0 for x in coins):
        raise ValueError('positive coins and nonnegative target required')
    ways = [0]*(target+1)
    ways[0] = 1
    for coin in sorted(set(coins)):
        for amount in range(coin, target+1):
            ways[amount] += ways[amount-coin]
    return ways[target]
