# Count contiguous alternating binary windows

Track the longest alternating suffix. Each new unequal neighboring bit extends it, while a repeated bit resets it. Add that suffix length because all its suffixes are also alternating.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/count_alternating_binary_subarrays.py)
- [Tests](../tests/test_count_alternating_binary_subarrays.py)

Run this exercise: `python -m unittest tests.test_count_alternating_binary_subarrays -v`
