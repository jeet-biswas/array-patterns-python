# Minimize the largest difference among disjoint pairs

Binary-search the allowed difference. On sorted values, greedily pairing adjacent eligible values maximizes how many disjoint pairs can be formed under that bound. D is the input value range. Exactly the requested number of pairs can be kept from any larger feasible matching.

Complexity: O(n log n + n log(D + 1)) time, O(n) space.

- [Implementation](../arrays/minimize_max_pair_difference.py)
- [Tests](../tests/test_minimize_max_pair_difference.py)

Run this exercise: `python -m unittest tests.test_minimize_max_pair_difference -v`
