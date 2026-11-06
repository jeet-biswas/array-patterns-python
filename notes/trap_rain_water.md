# Trapping rain water

Maintain the tallest wall encountered at each end. Resolve the side with the lower current wall: the opposite side guarantees a sufficient boundary. Bar widths are one unit.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/trap_rain_water.py)
- [Tests](../tests/test_trap_rain_water.py)

Run this exercise: `python -m unittest tests.test_trap_rain_water -v`
