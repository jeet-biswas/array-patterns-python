# Recover a nonnegative array from shuffled values and doubles

Process values in increasing order. Every unconsumed value must belong to the original array and needs one matching double. Zero consumes two copies of itself. Return None when pairing is impossible, distinguishing failure from an empty original.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/recover_doubled_array.py)
- [Tests](../tests/test_recover_doubled_array.py)

Run this exercise: `python -m unittest tests.test_recover_doubled_array -v`
