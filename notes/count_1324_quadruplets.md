# Count strict 1324-pattern index quadruplets

For each prospective second index, store the number of earlier 132 triplets using it as the high middle value. A later larger value completes those triplets. When the current value is smaller instead, count earlier values below it to create new triplets. Strict comparisons exclude ties.

Complexity: O(n squared) time, O(n) space.

- [Implementation](../arrays/count_1324_quadruplets.py)
- [Tests](../tests/test_count_1324_quadruplets.py)

Run this exercise: `python -m unittest tests.test_count_1324_quadruplets -v`
