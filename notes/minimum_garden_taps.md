# Minimum radius-array taps covering a continuous garden

Convert each tap radius into a clipped interval and record the furthest right endpoint for each left boundary. Sweep possible starts, extending the best frontier; when reaching the current covered boundary, commit one tap to the furthest available endpoint. Failure to advance reveals an uncovered gap.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/minimum_garden_taps.py)
- [Tests](../tests/test_minimum_garden_taps.py)

Run this exercise: `python -m unittest tests.test_minimum_garden_taps -v`
