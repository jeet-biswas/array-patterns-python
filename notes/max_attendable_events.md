# Attend the most events with one event per integer day

Sort by start day and keep available event deadlines in a min-heap. Attend the event expiring first, discard expired events, and jump to the next start when no event is available. The number of day advances is bounded by the number of attended events.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/max_attendable_events.py)
- [Tests](../tests/test_max_attendable_events.py)

Run this exercise: `python -m unittest tests.test_max_attendable_events -v`
