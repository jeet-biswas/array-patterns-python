# Largest array total after one matching segment exchange

Exchanging one segment changes the first total by the sum of second-minus-first differences on that segment. Kadane scans find the best gain in each direction, allowing an empty exchange. Apply each gain to its original total and keep the larger.

Complexity: O(n) time, O(1) auxiliary space.

- [Implementation](../arrays/max_spliced_array_sum.py)
- [Tests](../tests/test_max_spliced_array_sum.py)

Run this exercise: `python -m unittest tests.test_max_spliced_array_sum -v`
