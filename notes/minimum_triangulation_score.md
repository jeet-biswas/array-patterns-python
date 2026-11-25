# Minimum triangulation score of a cyclic value array

Values label the ordered vertices of a convex polygon. For each interval, choose the triangle incident to its boundary edge; its third vertex divides the remaining work into two smaller intervals. A triangle costs the product of its three labels.

Complexity: O(n cubed) time, O(n squared) space.

- [Implementation](../arrays/minimum_triangulation_score.py)
- [Tests](../tests/test_minimum_triangulation_score.py)

Run this exercise: `python -m unittest tests.test_minimum_triangulation_score -v`
