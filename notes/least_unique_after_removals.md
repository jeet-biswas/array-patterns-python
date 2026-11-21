# Fewest distinct values after exactly k deletions

Deleting all occurrences of a value reduces the distinct count by one. Spend the deletion budget on the smallest frequencies first; partially deleting the next group cannot reduce the distinct count further. u is the initial number of distinct values.

Complexity: O(n + u log u) time, O(u) space.

- [Implementation](../arrays/least_unique_after_removals.py)
- [Tests](../tests/test_least_unique_after_removals.py)

Run this exercise: `python -m unittest tests.test_least_unique_after_removals -v`
