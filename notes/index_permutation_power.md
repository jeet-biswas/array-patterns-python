# Raise an index permutation to any signed integer power

Decompose the permutation into cycles. Applying it exponent times advances each cycle position by exponent modulo the cycle length; negative powers move backward. Runtime does not depend on the exponent magnitude except for integer remainder cost.

Complexity: O(n) index operations, O(n) space.

- [Implementation](../arrays/index_permutation_power.py)
- [Tests](../tests/test_index_permutation_power.py)

Run this exercise: `python -m unittest tests.test_index_permutation_power -v`
