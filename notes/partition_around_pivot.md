# Partition an array into less-than, equal and greater-than regions

Maintain completed less-than and greater-than regions around an unclassified middle. A small value moves to the left boundary, a large value to the right boundary, and an equal value advances the scan. A swapped-in unclassified value must be examined again.

Complexity: O(n) time, O(1) auxiliary space.

- [Implementation](../arrays/partition_around_pivot.py)
- [Tests](../tests/test_partition_around_pivot.py)

Run this exercise: `python -m unittest tests.test_partition_around_pivot -v`
