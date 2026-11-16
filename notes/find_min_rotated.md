# Minimum in a rotated array with duplicates

Compare the midpoint to the right endpoint to identify a half containing the minimum. Equal endpoints hide the pivot direction, so discard one duplicate endpoint. This ambiguity explains the linear worst case.

Complexity: O(log n) typical, O(n) worst-case time, O(1) space.

- [Implementation](../arrays/find_min_rotated.py)
- [Tests](../tests/test_find_min_rotated.py)

Run this exercise: `python -m unittest tests.test_find_min_rotated -v`
