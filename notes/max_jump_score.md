# Maximum score with bounded forward jumps

Dynamic programming chooses the best reachable predecessor. A decreasing deque keeps only useful scores within k positions, so each position enters and leaves once. Both endpoints must be visited.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/max_jump_score.py)
- [Tests](../tests/test_max_jump_score.py)

Run this exercise: `python -m unittest tests.test_max_jump_score -v`
