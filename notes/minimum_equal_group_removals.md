# Empty an array by removing equal-value pairs or triples

Each value frequency is independent. A singleton is impossible to remove; every larger frequency needs ceiling(count/3) operations because pairs handle the one- or two-element remainder without increasing that lower bound.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/minimum_equal_group_removals.py)
- [Tests](../tests/test_minimum_equal_group_removals.py)

Run this exercise: `python -m unittest tests.test_minimum_equal_group_removals -v`
