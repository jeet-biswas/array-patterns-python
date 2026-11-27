# Fewest deletions leaving an even array of unequal neighbor pairs

Keep the first element of each prospective pair, then skip equal values until an unequal partner appears. Choosing the earliest valid partner leaves the most suffix available. If one unpaired element remains at the end, delete it too.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/minimum_deletions_unequal_pairs.py)
- [Tests](../tests/test_minimum_deletions_unequal_pairs.py)

Run this exercise: `python -m unittest tests.test_minimum_deletions_unequal_pairs -v`
