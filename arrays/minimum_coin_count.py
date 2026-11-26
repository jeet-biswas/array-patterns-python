def minimum_coin_count(coins: list[int], target: int) -> int | None:
    """Fewest coins summing to target, with unlimited reuse; None if impossible.

    Positive denominations, nonnegative target required. Duplicates ignored; no mutation.
    """
    if target < 0 or any(x <= 0 for x in coins):
        raise ValueError('positive coins and nonnegative target required')
    unique = sorted(set(coins))
    counts = [target+1]*(target+1)
    counts[0] = 0
    for amount in range(1, target+1):
        for coin in unique:
            if coin > amount: break
            counts[amount] = min(counts[amount], counts[amount-coin]+1)
    return counts[target] if counts[target] <= target else None
