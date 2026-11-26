# Longest reorderable chain of repeated squaring

Process distinct values in descending order. The longest chain starting at x extends the already processed state for x squared, when present. Values are at least two, so chains strictly increase and duplicate copies cannot extend them. u is the number of distinct values; big-integer operation costs depend on value width.

Complexity: O(n + u log u) arithmetic operations, O(u) space.

- [Implementation](../arrays/longest_square_streak.py)
- [Tests](../tests/test_longest_square_streak.py)

Run this exercise: `python -m unittest tests.test_longest_square_streak -v`
