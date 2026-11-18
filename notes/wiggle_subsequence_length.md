# Longest alternating-difference subsequence

Track the best lengths ending with an upward or downward difference. A rise extends the previous downward state; a fall extends the upward state. Equal adjacent readings add no useful change, and repeated moves in one direction replace an endpoint rather than extending the sequence.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/wiggle_subsequence_length.py)
- [Tests](../tests/test_wiggle_subsequence_length.py)

Run this exercise: `python -m unittest tests.test_wiggle_subsequence_length -v`
