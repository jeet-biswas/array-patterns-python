# Range sums with position-relative weights

Store ordinary prefix sums and global index-weighted prefix sums. Subtract start times the ordinary range sum from the weighted range sum to shift weights from global indices to 1, 2, ..., interval length.

Complexity: O(n) build/space, O(1) per query.

- [Implementation](../arrays/weighted_range_sum.py)
- [Tests](../tests/test_weighted_range_sum.py)

Run this exercise: `python -m unittest tests.test_weighted_range_sum -v`
