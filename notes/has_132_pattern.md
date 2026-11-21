# Detect a strict 132 pattern in an array

Scan right to left with a decreasing stack of possible high values. Popping a smaller value certifies it as a middle value below a high value to its left. Any later-scanned value strictly below that certified middle completes the pattern.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/has_132_pattern.py)
- [Tests](../tests/test_has_132_pattern.py)

Run this exercise: `python -m unittest tests.test_has_132_pattern -v`
