# Minimum end removals with a target sum

Removing elements only from the ends leaves one contiguous middle. Maximize the retained length with sum total minus the requested removal sum, using earliest prefix-sum positions. Signed values work without a positive-only sliding-window assumption.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/min_end_removals_sum.py)
- [Tests](../tests/test_min_end_removals_sum.py)

Run this exercise: `python -m unittest tests.test_min_end_removals_sum -v`
