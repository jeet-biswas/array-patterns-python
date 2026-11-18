# Maximum index-weighted rotation score

For a right rotation, every value gains one index weight except the former last value, whose weight drops by n-1. Update the score by total minus n times that value instead of constructing each rotation.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/max_rotation_score.py)
- [Tests](../tests/test_max_rotation_score.py)

Run this exercise: `python -m unittest tests.test_max_rotation_score -v`
