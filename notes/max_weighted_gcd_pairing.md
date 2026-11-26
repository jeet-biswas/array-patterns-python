# Maximize round-weighted GCD scores over disjoint pairs

A bitmask records used indices. The number of used pairs determines the next round multiplier, so the mask alone identifies the state. Try every unused pair and memoize the best continuation. Unlike unweighted matching, fixing a particular first index would miss valid round assignments. Intended for small even-length arrays.

Complexity: O(n squared 2^n) time, O(2^n + n squared) space.

- [Implementation](../arrays/max_weighted_gcd_pairing.py)
- [Tests](../tests/test_max_weighted_gcd_pairing.py)

Run this exercise: `python -m unittest tests.test_max_weighted_gcd_pairing -v`
