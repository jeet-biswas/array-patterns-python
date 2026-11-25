# Fewest decrements to make alternating strict valleys

Try each parity as the valley positions. Decrease each valley below its smaller neighbor, leaving peaks unchanged. Decreasing a peak could only make its neighboring valley requirements harder, so an optimal solution exists with unchanged peaks.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/minimum_decrements_zigzag.py)
- [Tests](../tests/test_minimum_decrements_zigzag.py)

Run this exercise: `python -m unittest tests.test_minimum_decrements_zigzag -v`
