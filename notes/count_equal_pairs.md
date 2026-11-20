# Count equal-value index pairs

When a new value arrives, it forms one new pair with each identical earlier value. Add the previous frequency before incrementing it, counting each unordered index pair exactly once.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/count_equal_pairs.py)
- [Tests](../tests/test_count_equal_pairs.py)

Run this exercise: `python -m unittest tests.test_count_equal_pairs -v`
