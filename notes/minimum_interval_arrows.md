# Fewest points needed to hit all closed intervals

Sort intervals by their right endpoint. Place a point at the earliest uncovered endpoint; this is as far right as possible while still hitting that interval, so it preserves every future opportunity. Closed intervals sharing that point are covered together.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/minimum_interval_arrows.py)
- [Tests](../tests/test_minimum_interval_arrows.py)

Run this exercise: `python -m unittest tests.test_minimum_interval_arrows -v`
