# Minimum cutting cost for an array of cut positions

Sort the cut positions and add both stick endpoints. For each interval, try every required cut as its first cut: it costs the current interval length plus the optimal costs of the two resulting intervals. Increasing interval widths ensure those subproblems are already solved; m is the number of cuts.

Complexity: O(m cubed) time, O(m squared) space.

- [Implementation](../arrays/minimum_stick_cut_cost.py)
- [Tests](../tests/test_minimum_stick_cut_cost.py)

Run this exercise: `python -m unittest tests.test_minimum_stick_cut_cost -v`
