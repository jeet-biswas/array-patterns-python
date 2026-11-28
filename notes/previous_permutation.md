# Move to the previous lexicographic array permutation in place

Find the rightmost descent, swap its left value with the rightmost smaller suffix value, then reverse the suffix to make it as large as possible. If there is no descent, reverse the whole array to wrap to the largest permutation.

Complexity: O(n) time, O(1) auxiliary space.

- [Implementation](../arrays/previous_permutation.py)
- [Tests](../tests/test_previous_permutation.py)

Run this exercise: `python -m unittest tests.test_previous_permutation -v`
