# Maximum bitwise AND of two elements

Build the result from high bits to low bits. A candidate mask is attainable exactly when at least two elements contain all of its bits. Keeping an attainable higher bit always dominates any combination of lower bits.

Complexity: O(nB) bit checks, O(1) auxiliary slots.

- [Implementation](../arrays/max_and_pair.py)
- [Tests](../tests/test_max_and_pair.py)

Run this exercise: `python -m unittest tests.test_max_and_pair -v`
