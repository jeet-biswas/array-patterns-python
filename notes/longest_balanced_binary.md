# Longest subarray with equal zeros and ones

Treat zero as minus one and one as plus one. Equal prefix balances enclose a balanced subarray. Store the earliest occurrence of each balance to maximize the length.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/longest_balanced_binary.py)
- [Tests](../tests/test_longest_balanced_binary.py)

Run this exercise: `python -m unittest tests.test_longest_balanced_binary -v`
