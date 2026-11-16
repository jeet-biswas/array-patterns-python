# Smallest ordered prefix-suffix partition

Maintain the maximum committed to the left partition and the maximum seen overall. A value below the committed maximum must join the left partition, extending its boundary and adopting the overall maximum.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/partition_disjoint.py)
- [Tests](../tests/test_partition_disjoint.py)

Run this exercise: `python -m unittest tests.test_partition_disjoint -v`
