# Closest triplet sum with deterministic ties

For each fixed value in a sorted copy, move the pair sum toward the target. Compare candidates by absolute error and then by sum, so ties consistently select the smaller sum.

Complexity: O(n squared) time, O(n) space.

- [Implementation](../arrays/three_sum_closest.py)
- [Tests](../tests/test_three_sum_closest.py)

Run this exercise: `python -m unittest tests.test_three_sum_closest -v`
