# Count subsequences with bounded minimum-plus-maximum

Sort a copy and fix the smallest selected occurrence. If the largest allowed occurrence can pair with it, any subset of the intervening positions is valid, giving a power-of-two count. Sorting preserves the number of index-distinct selections.

Complexity: O(n log n) comparisons, O(n) auxiliary slots.

- [Implementation](../arrays/count_subsequences_minmax.py)
- [Tests](../tests/test_count_subsequences_minmax.py)

Run this exercise: `python -m unittest tests.test_count_subsequences_minmax -v`
