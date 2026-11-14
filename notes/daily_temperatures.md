# Days until a warmer temperature

Store unresolved day indices on a decreasing temperature stack. A warmer reading resolves all colder days on top, recording the distance in days. Equal temperatures remain unresolved.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/daily_temperatures.py)
- [Tests](../tests/test_daily_temperatures.py)

Run this exercise: `python -m unittest tests.test_daily_temperatures -v`
