# Stock profit with a fee per completed trade

Keep the best cash balance and best balance while holding one share. Selling subtracts the fee exactly once; buying and selling transitions both use the previous day's states.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/max_profit_fee.py)
- [Tests](../tests/test_max_profit_fee.py)

Run this exercise: `python -m unittest tests.test_max_profit_fee -v`
