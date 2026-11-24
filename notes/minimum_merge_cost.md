# Minimum total cost of merging array weights in pairs

Repeatedly merge the two smallest weights and return their sum to a min-heap. An optimal merge tree can place the two smallest weights as deepest siblings, justifying this greedy reduction. This allows arbitrary pairs, unlike merging adjacent intervals.

Complexity: O(n log(n + 1)) time, O(n) space.

- [Implementation](../arrays/minimum_merge_cost.py)
- [Tests](../tests/test_minimum_merge_cost.py)

Run this exercise: `python -m unittest tests.test_minimum_merge_cost -v`
