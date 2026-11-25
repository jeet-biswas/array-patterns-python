# Minimum cost to merge adjacent groups of k piles

Each merge reduces the pile count by k-1, giving the feasibility condition. Interval DP stores the cost of reducing each interval as far as possible. Split at offsets spaced k-1 apart, and charge the full interval sum exactly when it can collapse to one pile.

Complexity: O(n cubed) time, O(n squared) space.

- [Implementation](../arrays/minimum_adjacent_k_merge_cost.py)
- [Tests](../tests/test_minimum_adjacent_k_merge_cost.py)

Run this exercise: `python -m unittest tests.test_minimum_adjacent_k_merge_cost -v`
