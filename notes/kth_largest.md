# Kth largest array element

Keep a min-heap containing the largest k values seen. Its root is the kth largest, with duplicate values counted separately. This avoids sorting the entire input.

Complexity: O(n log(k + 1)) time, O(k) space.

- [Implementation](../arrays/kth_largest.py)
- [Tests](../tests/test_kth_largest.py)

Run this exercise: `python -m unittest tests.test_kth_largest -v`
