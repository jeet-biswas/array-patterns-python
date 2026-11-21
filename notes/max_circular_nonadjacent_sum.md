# Maximum nonadjacent sum on a circular array

The first and last positions cannot both be selected. Solve two linear ranges, each excluding one endpoint, and keep the larger result. Each linear scan keeps only the best one-step and two-step histories.

Complexity: O(n) time, O(1) auxiliary space.

- [Implementation](../arrays/max_circular_nonadjacent_sum.py)
- [Tests](../tests/test_max_circular_nonadjacent_sum.py)

Run this exercise: `python -m unittest tests.test_max_circular_nonadjacent_sum -v`
