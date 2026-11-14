# Unique quadruplets with a target sum

Sort a copy, fix two positions, then use a two-pointer sweep for the remaining pair. Skip repeated fixed values and matched endpoints, returning each sorted value quadruplet once in lexicographic order.

Complexity: O(n cubed) time, O(n) auxiliary space plus output.

- [Implementation](../arrays/four_sum.py)
- [Tests](../tests/test_four_sum.py)

Run this exercise: `python -m unittest tests.test_four_sum -v`
