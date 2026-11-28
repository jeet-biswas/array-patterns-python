# Find missing domain values using reversible sign marking

Each value marks its corresponding index negative. Unmarked indices identify missing values. Restore every entry to positive before returning, preserving the original array exactly. Validate first so malformed input cannot leave partial markings.

Complexity: O(n) time, O(1) auxiliary space beyond output.

- [Implementation](../arrays/missing_numbers_one_to_n.py)
- [Tests](../tests/test_missing_numbers_one_to_n.py)

Run this exercise: `python -m unittest tests.test_missing_numbers_one_to_n -v`
