# Count subarrays with exact minimum and maximum

Remember the last occurrence of each required bound and the last out-of-range value. A valid start must follow the out-of-range position and precede both bound occurrences. Equal bounds are handled by the same rule.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/count_fixed_bounds.py)
- [Tests](../tests/test_count_fixed_bounds.py)

Run this exercise: `python -m unittest tests.test_count_fixed_bounds -v`
