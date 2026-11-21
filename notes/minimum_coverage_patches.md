# Fewest patches to cover every subset sum up to a target

Maintain the smallest positive sum not yet representable. A next value at most that boundary extends coverage by its value. Otherwise add the boundary itself: it fills the first gap and doubles the covered range, which is the largest possible extension without leaving that gap.

Complexity: O(n + log(target + 1)) time, O(1) auxiliary space.

- [Implementation](../arrays/minimum_coverage_patches.py)
- [Tests](../tests/test_minimum_coverage_patches.py)

Run this exercise: `python -m unittest tests.test_minimum_coverage_patches -v`
