def stock_spans(prices: list[int]) -> list[int]:
    """For each reading, count consecutive days ending there with price <= it.

    Includes the current day; integer readings may be signed.
    O(n) time, O(n) space including output; input is unchanged.
    """
    stack = []
    result = []
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] <= price:
            stack.pop()
        result.append(i - stack[-1] if stack else i + 1)
        stack.append(i)
    return result
