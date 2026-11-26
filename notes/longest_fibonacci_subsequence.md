# Longest subsequence where each value sums the preceding two

A pair of final indices determines a Fibonacci-like state. For each pair, look up the unique earlier value equal to their difference and extend its pair state. Strictly increasing positive values make this predecessor unique and preserve index order.

Complexity: Expected O(n squared) time, O(n squared) space.

- [Implementation](../arrays/longest_fibonacci_subsequence.py)
- [Tests](../tests/test_longest_fibonacci_subsequence.py)

Run this exercise: `python -m unittest tests.test_longest_fibonacci_subsequence -v`
