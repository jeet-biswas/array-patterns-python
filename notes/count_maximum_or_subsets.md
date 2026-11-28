# Count nonempty index subsets attaining the largest bitwise OR

Track counts of subsets by their OR value, copying each layer before adding the current index. The largest possible OR is the OR of the full array. Remove the empty subset only when that target is zero. R is the number of reachable OR states; arithmetic and bitwise costs depend on integer width.

Complexity: Expected O(nR) map/bitwise operations, O(R) states.

- [Implementation](../arrays/count_maximum_or_subsets.py)
- [Tests](../tests/test_count_maximum_or_subsets.py)

Run this exercise: `python -m unittest tests.test_count_maximum_or_subsets -v`
