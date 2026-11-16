# Duplicate zeros in a fixed-length array

Count the virtual extra slots needed for zero copies, then write backwards as if the array had expanded. Only writes within the original length are retained, so shifted elements at the end are discarded.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/duplicate_zeros.py)
- [Tests](../tests/test_duplicate_zeros.py)

Run this exercise: `python -m unittest tests.test_duplicate_zeros -v`
