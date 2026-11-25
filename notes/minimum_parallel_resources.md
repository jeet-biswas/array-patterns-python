# Minimum resources for overlapping half-open intervals

Sweep sorted arrival and departure events, handling departures before arrivals at the same position. The maximum simultaneous occupancy is both a necessary lower bound and achievable by reusing resources as intervals finish.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/minimum_parallel_resources.py)
- [Tests](../tests/test_minimum_parallel_resources.py)

Run this exercise: `python -m unittest tests.test_minimum_parallel_resources -v`
