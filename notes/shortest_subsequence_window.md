# Shortest contiguous window containing an ordered subsequence

For each pattern prefix, track the latest possible start of a matching subsequence ending no later than the current position. Update pattern positions backward so one source element cannot be reused. A completed match with the latest start is the shortest candidate at that endpoint.

Complexity: O(nm) time, O(m) auxiliary space.

- [Implementation](../arrays/shortest_subsequence_window.py)
- [Tests](../tests/test_shortest_subsequence_window.py)

Run this exercise: `python -m unittest tests.test_shortest_subsequence_window -v`
