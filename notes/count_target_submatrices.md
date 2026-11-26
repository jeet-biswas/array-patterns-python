# Count rectangular submatrices with a target sum

Fix each top and bottom row and accumulate their column totals. Each target-sum subarray of those totals represents exactly one rectangle. A prefix-sum frequency map counts these subarrays, including signed values and repeated prefix sums.

Complexity: O(r + r squared c) expected time, O(c) auxiliary space.

- [Implementation](../arrays/count_target_submatrices.py)
- [Tests](../tests/test_count_target_submatrices.py)

Run this exercise: `python -m unittest tests.test_count_target_submatrices -v`
