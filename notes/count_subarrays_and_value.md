# Count contiguous subarrays with a specified bitwise AND

Group all suffixes ending at the current position by their AND value and retain their multiplicities. Extending a suffix can only clear bits, so at most B+1 distinct states survive at an endpoint. B is the maximum value bit width, at least one.

Complexity: Expected O(nB) map/bitwise operations, O(B) states.

- [Implementation](../arrays/count_subarrays_and_value.py)
- [Tests](../tests/test_count_subarrays_and_value.py)

Run this exercise: `python -m unittest tests.test_count_subarrays_and_value -v`
