# Pair a signed array into value-and-double pairs

Process distinct values by absolute magnitude so a required double has not already been treated as a smaller value. Match all copies at once. Zero must have even frequency; negative pairs work under the same ordering. u is the distinct-value count.

Complexity: O(n + u log u) time, O(u) space.

- [Implementation](../arrays/can_pair_doubles.py)
- [Tests](../tests/test_can_pair_doubles.py)

Run this exercise: `python -m unittest tests.test_can_pair_doubles -v`
