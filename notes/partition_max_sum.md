# Best sum after replacing blocks by their maxima

For each prefix, try every final block of length at most k. Maintain its maximum while extending backward, and combine its replacement sum with the best earlier prefix. Every element belongs to exactly one block.

Complexity: O(nk) time, O(n) space.

- [Implementation](../arrays/partition_max_sum.py)
- [Tests](../tests/test_partition_max_sum.py)

Run this exercise: `python -m unittest tests.test_partition_max_sum -v`
