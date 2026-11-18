# Resolve one-dimensional asteroid collisions

Only a right-moving survivor followed by a left-moving asteroid can collide. Resolve that pair by magnitude, repeating while the incoming asteroid survives. Each asteroid enters and leaves the stack at most once.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/asteroid_collision.py)
- [Tests](../tests/test_asteroid_collision.py)

Run this exercise: `python -m unittest tests.test_asteroid_collision -v`
