# Smallest common heater radius covering all house positions

Sort heater positions and binary-search the insertion point for each house. Its nearest heater is one of the two adjacent candidates. The largest nearest-heater distance is exactly the radius needed to cover every house.

Complexity: O(m log m + n log(m + 1)) time, O(m) space.

- [Implementation](../arrays/minimum_heater_radius.py)
- [Tests](../tests/test_minimum_heater_radius.py)

Run this exercise: `python -m unittest tests.test_minimum_heater_radius -v`
