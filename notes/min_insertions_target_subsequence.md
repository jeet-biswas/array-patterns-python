# Insert the fewest values to embed a distinct target

Map distinct target values to their positions. The longest increasing subsequence of mapped source positions is the longest target subsequence already present. Every unmatched target position requires one insertion; n is target length and m is source length.

Complexity: O(n + m log(n + 1)) time, O(n) space.

- [Implementation](../arrays/min_insertions_target_subsequence.py)
- [Tests](../tests/test_min_insertions_target_subsequence.py)

Run this exercise: `python -m unittest tests.test_min_insertions_target_subsequence -v`
