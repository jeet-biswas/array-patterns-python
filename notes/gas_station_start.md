# Find a feasible circular gas-station start

If a candidate start runs out of fuel at a station, every start between that candidate and the failure also fails. Reset the candidate to the next station. A nonnegative overall surplus guarantees the final candidate can complete the circuit.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/gas_station_start.py)
- [Tests](../tests/test_gas_station_start.py)

Run this exercise: `python -m unittest tests.test_gas_station_start -v`
