# Count all windows with a bounded value spread

Increasing and decreasing deques expose the window minimum and maximum. Advance the left edge until their difference is allowed; every suffix of that valid window also qualifies.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/count_bounded_spread_subarrays.py)
- [Tests](../tests/test_count_bounded_spread_subarrays.py)

Run this exercise: `python -m unittest tests.test_count_bounded_spread_subarrays -v`
