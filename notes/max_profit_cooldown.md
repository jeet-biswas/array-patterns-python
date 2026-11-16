# Maximum stock profit with a one-day cooldown

Track holding, just-sold, and resting states. Buying can only follow a resting day; selling moves to the just-sold state, which must pass through rest before buying again. Update all states from the previous day.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/max_profit_cooldown.py)
- [Tests](../tests/test_max_profit_cooldown.py)

Run this exercise: `python -m unittest tests.test_max_profit_cooldown -v`
