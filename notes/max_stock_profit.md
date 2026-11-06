# Best single buy/sell profit

Track the smallest price before each sell day. Returning zero allows no trade when prices only decrease. Prices must be nonnegative integers.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/max_stock_profit.py)
- [Tests](../tests/test_max_stock_profit.py)

Run this exercise: `python -m unittest tests.test_max_stock_profit -v`
