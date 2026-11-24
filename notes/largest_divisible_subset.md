# Recover a largest pairwise-divisible subset

Sort the values and find a longest chain where each predecessor divides its successor. Divisibility is transitive, so the chain is pairwise compatible. Parent indices reconstruct one optimal subset; ties keep the earliest sorted predecessor and endpoint.

Complexity: O(n squared) time, O(n) space.

- [Implementation](../arrays/largest_divisible_subset.py)
- [Tests](../tests/test_largest_divisible_subset.py)

Run this exercise: `python -m unittest tests.test_largest_divisible_subset -v`
