# Count contiguous partitions that never split equal values

Record the last occurrence of each value and sweep while tracking the furthest occurrence required by the current block. A cut is permitted exactly when that frontier ends at the current position. Each internal permitted cut can independently be kept or omitted, yielding a power of two. The result is exact and may be large.

Complexity: Expected O(n) arithmetic operations, O(n) space.

- [Implementation](../arrays/count_value_disjoint_partitions.py)
- [Tests](../tests/test_count_value_disjoint_partitions.py)

Run this exercise: `python -m unittest tests.test_count_value_disjoint_partitions -v`
