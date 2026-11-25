# Partition an array into equal pairs or valid triples

A prefix is valid if its last block is an equal pair, an equal triple, or three consecutive increasing integers and the preceding prefix is valid. The empty prefix seeds the recurrence.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/has_valid_block_partition.py)
- [Tests](../tests/test_has_valid_block_partition.py)

Run this exercise: `python -m unittest tests.test_has_valid_block_partition -v`
