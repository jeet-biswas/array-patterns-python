# Count strictly increasing contiguous subarrays

Every increasing run ending at the current position contributes one valid suffix per element in the run. Equal or decreasing adjacent values restart the run at length one.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/count_increasing_subarrays.py)
- [Tests](../tests/test_count_increasing_subarrays.py)

Run this exercise: `python -m unittest tests.test_count_increasing_subarrays -v`
