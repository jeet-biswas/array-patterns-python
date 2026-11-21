# Maximum subsequence sum with bounded index gaps

Each chosen endpoint extends the best positive score from the last k indices, or starts a new subsequence. Keep those candidate scores in decreasing order and expire old indices before querying.

Complexity: O(n) time, O(min(n, k)) auxiliary space.

- [Implementation](../arrays/constrained_subsequence_sum.py)
- [Tests](../tests/test_constrained_subsequence_sum.py)

Run this exercise: `python -m unittest tests.test_constrained_subsequence_sum -v`
