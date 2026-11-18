# Count valid triangle triplets

Sort lengths and fix the largest side. If the smallest-plus-largest candidate pair exceeds that side, every larger left candidate also works. Count those pairs in bulk, otherwise advance the smaller side.

Complexity: O(n squared) time, O(n) space.

- [Implementation](../arrays/triangle_count.py)
- [Tests](../tests/test_triangle_count.py)

Run this exercise: `python -m unittest tests.test_triangle_count -v`
