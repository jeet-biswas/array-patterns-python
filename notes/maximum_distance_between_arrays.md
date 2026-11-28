# Largest difference between values from different sorted arrays

Track the smallest and largest endpoints from earlier arrays. Before incorporating a new array, pair its maximum with the earlier minimum and its minimum with the earlier maximum. This ordering prevents accidentally taking both endpoints from the same array. m is the number of arrays; sortedness is an unchecked precondition.

Complexity: O(m) time, O(1) auxiliary space.

- [Implementation](../arrays/maximum_distance_between_arrays.py)
- [Tests](../tests/test_maximum_distance_between_arrays.py)

Run this exercise: `python -m unittest tests.test_maximum_distance_between_arrays -v`
