# Rotate an array in place

Normalize the rotation modulo the length, reverse the whole array, then reverse each partition. Negative steps rotate left. Avoid slices to retain constant auxiliary space.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/rotate_right.py)
- [Tests](../tests/test_rotate_right.py)

Run this exercise: `python -m unittest tests.test_rotate_right -v`
