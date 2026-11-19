# Medians of consecutive fixed-size windows

Maintain a sorted list of the current window. Binary search identifies the outgoing occurrence and the insertion position for the incoming value. List shifts cost O(k); this deliberately simple implementation does not claim heap-like logarithmic updates.

Complexity: O(nk + k log k) time, O(k) auxiliary space.

- [Implementation](../arrays/sliding_window_medians.py)
- [Tests](../tests/test_sliding_window_medians.py)

Run this exercise: `python -m unittest tests.test_sliding_window_medians -v`
