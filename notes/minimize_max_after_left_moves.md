# Minimize the largest value by transferring units left

The sum of each prefix cannot decrease under leftward transfers, so its ceiling average bounds the final maximum from below. The largest such bound is achievable: excess at later positions can be distributed into earlier spare capacity.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/minimize_max_after_left_moves.py)
- [Tests](../tests/test_minimize_max_after_left_moves.py)

Run this exercise: `python -m unittest tests.test_minimize_max_after_left_moves -v`
