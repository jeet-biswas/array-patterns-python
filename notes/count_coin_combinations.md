# Count unordered reusable-coin combinations for a target

Process distinct denominations one at a time, adding ways from amount-minus-coin while scanning amounts upward. This permits reuse of the current coin but prevents counting different orders of the same multiset. n counts input coins, d distinct coins, and T is the target.

Complexity: O(n + d log d + dT + T) time, O(d + T) space.

- [Implementation](../arrays/count_coin_combinations.py)
- [Tests](../tests/test_count_coin_combinations.py)

Run this exercise: `python -m unittest tests.test_count_coin_combinations -v`
