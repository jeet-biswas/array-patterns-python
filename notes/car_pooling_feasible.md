# Check vehicle capacity across trip intervals

Record passenger changes at each pickup and dropoff, combine events at equal positions, and sweep in order. Trips use half-open ranges, so passengers leaving at a position make room for passengers boarding there.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/car_pooling_feasible.py)
- [Tests](../tests/test_car_pooling_feasible.py)

Run this exercise: `python -m unittest tests.test_car_pooling_feasible -v`
