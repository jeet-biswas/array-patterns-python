# Intersect two sorted disjoint interval arrays

Compare the current interval from each array and emit their overlap. Advance the one that ends first, because it cannot intersect any later interval on the other side. Inputs use closed endpoints and must be sorted and internally disjoint.

Complexity: O(n + m) time, O(n + m) output space.

- [Implementation](../arrays/intersect_interval_arrays.py)
- [Tests](../tests/test_intersect_interval_arrays.py)

Run this exercise: `python -m unittest tests.test_intersect_interval_arrays -v`
