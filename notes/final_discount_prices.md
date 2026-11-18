# Apply the first eligible future price discount

Keep indices waiting for a later price no greater than their own. A new price resolves all eligible indices on the stack, discounting each exactly once. Equal prices are eligible and produce a zero final price.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/final_discount_prices.py)
- [Tests](../tests/test_final_discount_prices.py)

Run this exercise: `python -m unittest tests.test_final_discount_prices -v`
