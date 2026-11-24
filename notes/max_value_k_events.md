# Maximum value from at most k nonoverlapping events

Sort events by start and binary-search the first event starting strictly after each end. A DP layer for each allowed selection count either skips the event or combines its value with the previous layer at that successor. Closed event endpoints may not overlap.

Complexity: O(n log n + nk) time, O(n) space.

- [Implementation](../arrays/max_value_k_events.py)
- [Tests](../tests/test_max_value_k_events.py)

Run this exercise: `python -m unittest tests.test_max_value_k_events -v`
