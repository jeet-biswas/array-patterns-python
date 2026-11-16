# Add two decimal digit arrays

Add matching least-significant positions with a carry, treating an exhausted input as zero. Accumulate reversed result digits and reverse once at the end, avoiding conversion to a machine-sized integer.

Complexity: O(n + m) time, O(max(n, m)) output space.

- [Implementation](../arrays/add_digit_arrays.py)
- [Tests](../tests/test_add_digit_arrays.py)

Run this exercise: `python -m unittest tests.test_add_digit_arrays -v`
