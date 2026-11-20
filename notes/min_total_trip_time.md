# Minimum time for parallel workers to finish trips

A time limit t permits sum(t // worker_time) completed trips. This count is monotonic, so binary-search from zero to the time the fastest worker would need alone. Workers operate independently and may finish multiple trips.

Complexity: O(n log(T + 1)) time, O(1) space.

- [Implementation](../arrays/min_total_trip_time.py)
- [Tests](../tests/test_min_total_trip_time.py)

Run this exercise: `python -m unittest tests.test_min_total_trip_time -v`
