# Stock profit with a transaction limit

Maintain best holding and sold balances for each allowed transaction count, updating from the previous day. If the limit cannot bind, sum positive adjacent gains directly instead of allocating transaction states.

Complexity: O(n min(k, n)) time, O(min(k, n)) space.

- [Implementation](../arrays/max_profit_transactions.py)
- [Tests](../tests/test_max_profit_transactions.py)

Run this exercise: `python -m unittest tests.test_max_profit_transactions -v`
