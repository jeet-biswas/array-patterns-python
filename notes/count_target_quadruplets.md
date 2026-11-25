# Count index quadruplets with a target sum

Before choosing the third index, add every pair ending just before it to a sum-frequency map. Query complementary sums with each fourth index. This guarantees four ordered, distinct indices and counts multiplicities without deduplication.

Complexity: Expected O(n squared) time, O(n squared) space.

- [Implementation](../arrays/count_target_quadruplets.py)
- [Tests](../tests/test_count_target_quadruplets.py)

Run this exercise: `python -m unittest tests.test_count_target_quadruplets -v`
