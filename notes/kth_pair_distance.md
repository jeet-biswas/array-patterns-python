# Kth smallest absolute pair distance

Sort the values and binary-search a distance threshold. A two-pointer sweep counts pairs no farther apart than that threshold. The first threshold with at least k qualifying pairs is the kth distance, including repeated distances.

Complexity: O(n log n + n log(D + 1)) time, O(n) space.

- [Implementation](../arrays/kth_pair_distance.py)
- [Tests](../tests/test_kth_pair_distance.py)

Run this exercise: `python -m unittest tests.test_kth_pair_distance -v`
