# Count subarrays containing the global maximum at least k times

Find the global maximum, then move a window over its occurrences. Whenever the window has enough copies, discard left endpoints until it no longer does. Every discarded starting position yields a qualifying subarray at the current right endpoint.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/count_global_max_occurrences.py)
- [Tests](../tests/test_count_global_max_occurrences.py)

Run this exercise: `python -m unittest tests.test_count_global_max_occurrences -v`
