# Check whether every inversion is between neighbors

A nonlocal inversion ending at i exists exactly when a value before i-1 exceeds the current value. Track that prefix maximum. This works for arbitrary signed arrays and duplicates, not just permutations.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/only_local_inversions.py)
- [Tests](../tests/test_only_local_inversions.py)

Run this exercise: `python -m unittest tests.test_only_local_inversions -v`
