# Count subarrays divisible by a modulus

Two prefix sums give a divisible subarray when their remainders match. Count each remainder frequency, starting with the empty prefix. Python modulo keeps signed prefix sums consistent for a positive modulus.

Complexity: Expected O(n) time, O(min(n, k)) space.

- [Implementation](../arrays/count_subarrays_divisible.py)
- [Tests](../tests/test_count_subarrays_divisible.py)

Run this exercise: `python -m unittest tests.test_count_subarrays_divisible -v`
