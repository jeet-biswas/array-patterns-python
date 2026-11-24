# Hire from both array ends with a limited candidate pool

Maintain the first and last candidate pools in one heap keyed by cost then original index. After hiring, replenish only the side that supplied the selected worker. Two inward pointers prevent a worker appearing twice when the pools overlap; c is the smaller of n and twice the candidate count.

Complexity: O(n + (c + k) log(c + 1)) time, O(c) space.

- [Implementation](../arrays/total_hiring_cost.py)
- [Tests](../tests/test_total_hiring_cost.py)

Run this exercise: `python -m unittest tests.test_total_hiring_cost -v`
