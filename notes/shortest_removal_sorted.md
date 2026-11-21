# Shortest contiguous removal leaving a sorted array

Find a sorted suffix, then extend a sorted prefix. Advance the suffix boundary until the two retained pieces join in nondecreasing order. The removed gap is a candidate; neither pointer moves backward.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/shortest_removal_sorted.py)
- [Tests](../tests/test_shortest_removal_sorted.py)

Run this exercise: `python -m unittest tests.test_shortest_removal_sorted -v`
