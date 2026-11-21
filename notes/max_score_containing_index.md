# Largest minimum-times-length score containing an index

A monotone stack gives each value its maximal span as a minimum. Evaluate only spans containing the required index. Since values are nonnegative, expanding a span with the same minimum cannot lower its score.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/max_score_containing_index.py)
- [Tests](../tests/test_max_score_containing_index.py)

Run this exercise: `python -m unittest tests.test_max_score_containing_index -v`
