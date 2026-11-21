# Count arithmetic subsequences of length at least three

For each endpoint, map a difference to the number of subsequences of length at least two ending there. A pair starts a new state; extending an existing state contributes to the answer. Repeated values and index-distinct selections are counted separately.

Complexity: Expected O(n squared) time, O(n squared) space.

- [Implementation](../arrays/count_arithmetic_subsequences.py)
- [Tests](../tests/test_count_arithmetic_subsequences.py)

Run this exercise: `python -m unittest tests.test_count_arithmetic_subsequences -v`
