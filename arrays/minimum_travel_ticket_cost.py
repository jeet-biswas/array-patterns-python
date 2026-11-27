from bisect import bisect_left


def minimum_travel_ticket_cost(days: list[int], costs: list[int]) -> int:
    """Cover sorted distinct positive travel days with 1/7/30-day passes; no mutation.

    costs must contain three nonnegative prices. A pass bought on day d covers
    d through d+duration-1. Empty travel costs zero.
    """
    if len(costs) != 3 or any(x < 0 for x in costs):
        raise ValueError('three nonnegative prices required')
    if any(x <= 0 for x in days) or any(days[i-1] >= days[i] for i in range(1, len(days))):
        raise ValueError('strictly increasing positive days required')
    dp = [0]*(len(days)+1)
    for i in range(len(days)-1, -1, -1):
        dp[i] = min(price+dp[bisect_left(days, days[i]+duration)] for duration, price in zip((1, 7, 30), costs))
    return dp[0]
