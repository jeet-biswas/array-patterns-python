# Sort by iteratively merging runs of doubling length

Merge adjacent sorted runs of width one, two, four and so on, alternating source and destination buffers. Taking from the left on ties preserves stability. Iteration avoids recursive stack use, and the input remains unchanged.

Complexity: O(n log(n + 1)) time, O(n) space.

- [Implementation](../arrays/bottom_up_merge_sort.py)
- [Tests](../tests/test_bottom_up_merge_sort.py)

Run this exercise: `python -m unittest tests.test_bottom_up_merge_sort -v`
