# Largest rectangle in a histogram

Maintain indices of increasing bar heights. A shorter bar closes rectangles for popped heights; the remaining stack top determines the left boundary. A virtual zero-height bar flushes the stack without modifying the input.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/largest_histogram_rectangle.py)
- [Tests](../tests/test_largest_histogram_rectangle.py)

Run this exercise: `python -m unittest tests.test_largest_histogram_rectangle -v`
