# Maximize minimum distance between selected positions

Sort a copy of candidate positions and binary-search the minimum separation. Greedily selecting the earliest feasible next position leaves the most room for subsequent selections. Repeated coordinates represent different candidates and may force zero separation.

Complexity: O(n log n + n log(D + 1)) time, O(n) space.

- [Implementation](../arrays/max_min_distance.py)
- [Tests](../tests/test_max_min_distance.py)

Run this exercise: `python -m unittest tests.test_max_min_distance -v`
