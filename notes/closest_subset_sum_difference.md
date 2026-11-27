# Smallest distance from a target to any subset sum

Split the array in half and enumerate each half's subset sums. Sort one side, then binary-search the required complement for every sum on the other side. Only the neighbors of the insertion position can be closest. This meet-in-the-middle approach avoids enumerating every full subset.

Complexity: O(n 2^ceil(n/2)) time, O(2^ceil(n/2)) space.

- [Implementation](../arrays/closest_subset_sum_difference.py)
- [Tests](../tests/test_closest_subset_sum_difference.py)

Run this exercise: `python -m unittest tests.test_closest_subset_sum_difference -v`
