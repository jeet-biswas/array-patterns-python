# Fewest deletions to form a strict mountain subsequence

Compute strict increasing subsequence lengths ending at every index, and strict decreasing lengths starting there by scanning backward. A valid peak needs both lengths above one. The longest combined mountain determines how many original elements must be deleted.

Complexity: O(n log(n + 1)) time, O(n) space.

- [Implementation](../arrays/minimum_mountain_removals.py)
- [Tests](../tests/test_minimum_mountain_removals.py)

Run this exercise: `python -m unittest tests.test_minimum_mountain_removals -v`
