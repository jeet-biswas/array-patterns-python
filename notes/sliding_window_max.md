# Sliding window maximum

Maintain candidate indices in a decreasing deque. Expire indices outside the window and discard smaller candidates before adding each new value. Each index enters and leaves at most once.

Complexity: O(n) time, O(k) auxiliary space.

- [Implementation](../arrays/sliding_window_max.py)
- [Tests](../tests/test_sliding_window_max.py)

Run this exercise: `python -m unittest tests.test_sliding_window_max -v`
