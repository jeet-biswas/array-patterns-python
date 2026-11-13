# Unique zero-sum triplets

Sort a copy, fix one value, and move two pointers over the suffix. Skip equal fixed values and equal matched endpoints to return each value triplet once in lexicographic order.

Complexity: O(n squared) time, O(n) auxiliary space plus output.

- [Implementation](../arrays/three_sum.py)
- [Tests](../tests/test_three_sum.py)

Run this exercise: `python -m unittest tests.test_three_sum -v`
