# Maximum score from exactly k end picks

Start with all k picks from the left. Replace one left pick at a time with a right pick, evaluating every possible split without recomputing its sum. Negative values are supported because exactly k picks are required.

Complexity: O(k) time, O(1) space.

- [Implementation](../arrays/max_points_from_ends.py)
- [Tests](../tests/test_max_points_from_ends.py)

Run this exercise: `python -m unittest tests.test_max_points_from_ends -v`
