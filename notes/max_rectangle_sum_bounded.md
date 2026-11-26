# Largest rectangular sum not exceeding a limit

Compress row intervals into column sums. For each running prefix, binary-search the smallest earlier prefix at least current-minus-limit. Keep prefixes in a sorted Python list; insertion is linear, so the documented complexity includes that cost.

Complexity: O(r + r squared c squared) time, O(c) auxiliary space.

- [Implementation](../arrays/max_rectangle_sum_bounded.py)
- [Tests](../tests/test_max_rectangle_sum_bounded.py)

Run this exercise: `python -m unittest tests.test_max_rectangle_sum_bounded -v`
