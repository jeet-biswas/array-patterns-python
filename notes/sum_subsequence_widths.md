# Sum widths of all nonempty subsequences

In sorted order, position i is the designated maximum of 2^i selections and the designated minimum of 2^(n-1-i). Their difference gives its net contribution, with index order consistently breaking ties among equal values.

Complexity: O(n log n) comparisons, O(n) auxiliary slots.

- [Implementation](../arrays/sum_subsequence_widths.py)
- [Tests](../tests/test_sum_subsequence_widths.py)

Run this exercise: `python -m unittest tests.test_sum_subsequence_widths -v`
