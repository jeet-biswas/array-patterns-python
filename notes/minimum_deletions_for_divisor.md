# Delete the fewest values until the minimum divides another array

A value divides every target exactly when it divides their GCD. Sort the candidate values and find the first divisor of that GCD; every smaller value must be deleted, and every larger value may remain. n and m are input lengths; GCD bit costs are additional.

Complexity: O(n log n + m) GCD/arithmetic operations, O(n) space.

- [Implementation](../arrays/minimum_deletions_for_divisor.py)
- [Tests](../tests/test_minimum_deletions_for_divisor.py)

Run this exercise: `python -m unittest tests.test_minimum_deletions_for_divisor -v`
