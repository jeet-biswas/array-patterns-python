# Maximum width ramp

Retain only indices of new strict prefix minima as possible left endpoints. Scan right endpoints backwards; each candidate is removed as soon as it can form a ramp, which is its widest possible match.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/max_width_ramp.py)
- [Tests](../tests/test_max_width_ramp.py)

Run this exercise: `python -m unittest tests.test_max_width_ramp -v`
