# Search a rotated sorted array

With distinct elements, at least one side of the midpoint remains sorted. Use its endpoint bounds to decide whether the target lies in that half. Distinctness and rotated sortedness are unchecked preconditions.

Complexity: O(log n) time, O(1) space.

- [Implementation](../arrays/search_rotated.py)
- [Tests](../tests/test_search_rotated.py)

Run this exercise: `python -m unittest tests.test_search_rotated -v`
