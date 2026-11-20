# Choose paired indices for maximum sum-times-minimum

Visit paired entries in descending order of the second value, treating it as the current minimum. Maintain the k largest first-array values seen with a min-heap. Evaluate their sum times the current threshold; nonnegative values make this ordering valid.

Complexity: O(n log n + n log(k + 1)) time, O(n + k) space.

- [Implementation](../arrays/max_subsequence_score.py)
- [Tests](../tests/test_max_subsequence_score.py)

Run this exercise: `python -m unittest tests.test_max_subsequence_score -v`
