# Median after each array prefix

Maintain a max-heap of the lower half and a min-heap of the upper half. Keep the lower heap equal in size or one larger; its maximum and the upper minimum then determine each prefix median.

Complexity: O(n log(n + 1)) time, O(n) space.

- [Implementation](../arrays/running_medians.py)
- [Tests](../tests/test_running_medians.py)

Run this exercise: `python -m unittest tests.test_running_medians -v`
