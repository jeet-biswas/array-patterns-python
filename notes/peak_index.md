# Find a strict local peak

With unequal adjacent elements, an upward slope guarantees a peak to its right, while a downward slope guarantees one on its left. Treat the values beyond either endpoint as negative infinity.

Complexity: O(log(n + 1)) time, O(1) space.

- [Implementation](../arrays/peak_index.py)
- [Tests](../tests/test_peak_index.py)

Run this exercise: `python -m unittest tests.test_peak_index -v`
