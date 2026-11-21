# Count windows containing every distinct array value

Determine the required number of distinct values once. Maintain a frequency window and discard starts while it still contains every value. All discarded starts yield complete subarrays at the current endpoint.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/count_complete_subarrays.py)
- [Tests](../tests/test_count_complete_subarrays.py)

Run this exercise: `python -m unittest tests.test_count_complete_subarrays -v`
