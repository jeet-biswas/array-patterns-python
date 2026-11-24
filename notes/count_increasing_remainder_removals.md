# Count subarray deletions leaving a strictly increasing array

Find the longest increasing prefix. For each increasing suffix, shorten that prefix until the retained boundary values join strictly. Every shorter prefix is also compatible, including the empty prefix. Count suffix deletions separately; deleting the whole array is allowed.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/count_increasing_remainder_removals.py)
- [Tests](../tests/test_count_increasing_remainder_removals.py)

Run this exercise: `python -m unittest tests.test_count_increasing_remainder_removals -v`
