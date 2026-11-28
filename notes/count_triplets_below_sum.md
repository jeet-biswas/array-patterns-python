# Count index triplets below a strict sum threshold

Sort the values, fix the smallest chosen position, and use two pointers for the other pair. If their sum is below the target, every smaller right choice with that left pointer also works; count them together and advance left.

Complexity: O(n squared) time, O(n) space.

- [Implementation](../arrays/count_triplets_below_sum.py)
- [Tests](../tests/test_count_triplets_below_sum.py)

Run this exercise: `python -m unittest tests.test_count_triplets_below_sum -v`
