# Static half-open range XOR queries

Store the XOR before each array position. Combining the prefixes at stop and start cancels everything outside the half-open query interval. The structure snapshots the input and permits empty intervals.

Complexity: O(n) build/space, O(1) query operations.

- [Implementation](../arrays/xor_range_query.py)
- [Tests](../tests/test_xor_range_query.py)

Run this exercise: `python -m unittest tests.test_xor_range_query -v`
