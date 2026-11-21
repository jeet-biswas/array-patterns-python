# Fewest removals to make half-open intervals disjoint

Keep intervals greedily in increasing finish order. Choosing the earliest available finish leaves the most room for subsequent intervals. Subtract the number kept from the input length. Touching half-open intervals do not overlap.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/minimum_interval_removals.py)
- [Tests](../tests/test_minimum_interval_removals.py)

Run this exercise: `python -m unittest tests.test_minimum_interval_removals -v`
