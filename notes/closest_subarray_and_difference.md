# Closest bitwise-AND window value to a target

Maintain the distinct AND values of suffixes ending at each element. Compare each reachable value with the target and retain the smallest distance. Equal states can be merged because only the AND result, not the suffix length or multiplicity, matters.

Complexity: Expected O(nB) set/bitwise operations, O(B) states.

- [Implementation](../arrays/closest_subarray_and_difference.py)
- [Tests](../tests/test_closest_subarray_and_difference.py)

Run this exercise: `python -m unittest tests.test_closest_subarray_and_difference -v`
