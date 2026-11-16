# Maximum subarray sum with at most one deletion

Track the best subarray ending at each position with no deletion and with one deletion. A deleted-state transition either removes the current value from the previous undeleted subarray, or extends an already-deleted subarray. At least one retained value is required.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/max_subarray_one_deletion.py)
- [Tests](../tests/test_max_subarray_one_deletion.py)

Run this exercise: `python -m unittest tests.test_max_subarray_one_deletion -v`
