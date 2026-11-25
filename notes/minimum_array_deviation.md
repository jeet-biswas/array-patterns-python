# Minimize the range under parity-based value operations

Double each odd value once, placing every element at its maximum reachable value. Repeatedly halve the current even maximum while tracking the minimum. An odd maximum cannot be reduced, so further reductions of other elements cannot improve the range. M is the largest normalized value.

Complexity: O(n log(M + 1) log(n + 1)) time, O(n) space.

- [Implementation](../arrays/minimum_array_deviation.py)
- [Tests](../tests/test_minimum_array_deviation.py)

Run this exercise: `python -m unittest tests.test_minimum_array_deviation -v`
