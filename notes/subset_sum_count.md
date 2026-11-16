# Count subsets with a target sum

Map each reachable sum to its number of index-distinct subsets. Copy the previous counts for exclusions, then add inclusions from that previous state. Zero-valued elements double counts naturally; signed values need no special case.

Complexity: Expected O(nR) time, O(R) space.

- [Implementation](../arrays/subset_sum_count.py)
- [Tests](../tests/test_subset_sum_count.py)

Run this exercise: `python -m unittest tests.test_subset_sum_count -v`
