# Largest pair sum among values with equal decimal digit sums

Compute each value's digit sum using its absolute magnitude. Retain the largest earlier value for each digit sum, since it is always the best partner for the current value. None distinguishes missing pairs from valid negative pair sums. D bounds decimal digit count.

Complexity: O(nD) digit operations, O(n) space.

- [Implementation](../arrays/max_pair_sum_equal_digit_sum.py)
- [Tests](../tests/test_max_pair_sum_equal_digit_sum.py)

Run this exercise: `python -m unittest tests.test_max_pair_sum_equal_digit_sum -v`
