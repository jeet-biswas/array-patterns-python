# Count nonempty index subsets avoiding a fixed value difference

Group distinct values by remainder modulo k. Only neighboring values separated by exactly k conflict within a group. A value with frequency c can be chosen in 2^c-1 nonempty index subsets. Apply take/skip DP along each sorted group, multiply independent group totals, then exclude the empty subset. u is the distinct value count; big-integer arithmetic costs grow with result width.

Complexity: O(n + u log u) arithmetic operations, O(u) auxiliary slots.

- [Implementation](../arrays/count_subsets_avoiding_difference.py)
- [Tests](../tests/test_count_subsets_avoiding_difference.py)

Run this exercise: `python -m unittest tests.test_count_subsets_avoiding_difference -v`
