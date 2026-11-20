# Count pairs below a strict sum threshold

Sort a copy and compare the two ends. If their sum is below the threshold, the left value also pairs successfully with every intermediate value. Otherwise reduce the right endpoint.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/count_pairs_below_sum.py)
- [Tests](../tests/test_count_pairs_below_sum.py)

Run this exercise: `python -m unittest tests.test_count_pairs_below_sum -v`
