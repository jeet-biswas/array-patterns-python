# Longest interval with a strict majority above a threshold

Map values above the threshold to +1 and others to -1. A qualifying interval has positive signed sum. Store earliest occurrences of prefix balances; a positive balance qualifies the whole prefix, otherwise the earliest balance one lower gives the longest candidate.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/longest_majority_above_threshold.py)
- [Tests](../tests/test_longest_majority_above_threshold.py)

Run this exercise: `python -m unittest tests.test_longest_majority_above_threshold -v`
