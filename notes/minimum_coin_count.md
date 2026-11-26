# Fewest reusable coin denominations needed for a target

For each amount, choose the best predecessor amount obtained by removing one available denomination. Normalize duplicate denominations so they do not change the problem. Positive coins make smaller amounts valid predecessor states; d is distinct denomination count and T the target.

Complexity: O(n + d log d + dT + T) time, O(d + T) space.

- [Implementation](../arrays/minimum_coin_count.py)
- [Tests](../tests/test_minimum_coin_count.py)

Run this exercise: `python -m unittest tests.test_minimum_coin_count -v`
