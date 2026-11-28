# Minimize squared paired differences with a unit-change budget

Each useful operation reduces a positive absolute difference by one. Larger differences give the largest decrease in squared cost. Binary-search a level to which every larger difference can be lowered within budget, then spend the remaining budget on one-step reductions at that level. D is the largest original difference.

Complexity: O(n log(D + 1)) time, O(n) space.

- [Implementation](../arrays/minimum_squared_pair_difference.py)
- [Tests](../tests/test_minimum_squared_pair_difference.py)

Run this exercise: `python -m unittest tests.test_minimum_squared_pair_difference -v`
