# Minimum forward jumps to the last index

Each greedy frontier represents positions reachable using the current number of jumps. Track the farthest next frontier while scanning it, and count a jump when reaching its boundary. Detect a stuck frontier instead of assuming reachability.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/min_jumps.py)
- [Tests](../tests/test_min_jumps.py)

Run this exercise: `python -m unittest tests.test_min_jumps -v`
