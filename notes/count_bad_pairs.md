# Count pairs violating the index-value difference rule

A good pair satisfies values[j]-j == values[i]-i. For each right index, subtract the number of matching transformed keys from the total earlier positions to count new bad pairs.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/count_bad_pairs.py)
- [Tests](../tests/test_count_bad_pairs.py)

Run this exercise: `python -m unittest tests.test_count_bad_pairs -v`
