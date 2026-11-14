# Count smaller elements to the right

Compress distinct values into ranks and scan backwards. A Fenwick array tracks frequencies of ranks already seen. Query the prefix before the current rank to exclude equal elements.

Complexity: O(n log(n + 1)) time, O(n) space.

- [Implementation](../arrays/count_smaller_right.py)
- [Tests](../tests/test_count_smaller_right.py)

Run this exercise: `python -m unittest tests.test_count_smaller_right -v`
