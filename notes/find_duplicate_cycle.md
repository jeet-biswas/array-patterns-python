# Find a repeated domain value by cycle detection

Interpret each value as the next index, starting from index zero. The repeated value is the reachable cycle entrance. Floyd's fast/slow pointers locate a meeting point, and a second walk from zero locates the entrance without changing the array.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/find_duplicate_cycle.py)
- [Tests](../tests/test_find_duplicate_cycle.py)

Run this exercise: `python -m unittest tests.test_find_duplicate_cycle -v`
