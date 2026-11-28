# Select the most frequent values with deterministic ties

Count occurrences, then retain the k strongest frequency/value pairs in a min heap. Larger frequency is better; for equal frequencies a smaller value is better. Sort the selected results by that same public order. u is the number of distinct values.

Complexity: O(n + u log(k + 1) + k log(k + 1)) time, O(u + k) space.

- [Implementation](../arrays/top_k_frequent_values.py)
- [Tests](../tests/test_top_k_frequent_values.py)

Run this exercise: `python -m unittest tests.test_top_k_frequent_values -v`
