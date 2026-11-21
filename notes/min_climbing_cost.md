# Minimum cost to climb an array of steps

The cost to reach each position is the smaller of paying for the previous step or the step before it. Positions zero and one are free starting positions; the destination is just beyond the array.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/min_climbing_cost.py)
- [Tests](../tests/test_min_climbing_cost.py)

Run this exercise: `python -m unittest tests.test_min_climbing_cost -v`
