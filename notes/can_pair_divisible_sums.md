# Pair all elements so each pair sum is divisible

Match remainder r with its complement -r modulo the modulus. Complement counts must agree; self-complementary remainders, including zero, require even counts. Python modulo handles negative array values consistently.

Complexity: Expected O(n) time, O(min(n, modulus)) space.

- [Implementation](../arrays/can_pair_divisible_sums.py)
- [Tests](../tests/test_can_pair_divisible_sums.py)

Run this exercise: `python -m unittest tests.test_can_pair_divisible_sums -v`
