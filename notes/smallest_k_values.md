# Select the k smallest array values in sorted order

Keep a max heap containing the smallest k values seen so far. Any smaller incoming value replaces the current largest retained value. Sorting the retained heap yields a deterministic ascending result, counting duplicates separately.

Complexity: O(n log(k + 1) + k) time, O(k) space.

- [Implementation](../arrays/smallest_k_values.py)
- [Tests](../tests/test_smallest_k_values.py)

Run this exercise: `python -m unittest tests.test_smallest_k_values -v`
