# Count target-sum triplets with duplicate index multiplicities

Count values and enumerate sorted value pairs x <= y, deriving z from the target. Enforce y <= z to avoid duplicate value triples. Use combinations when two or three values coincide, and multiply frequencies for three distinct values. u is the distinct value count.

Complexity: O(n + u squared) time, O(u) space.

- [Implementation](../arrays/count_triplets_target_multiplicity.py)
- [Tests](../tests/test_count_triplets_target_multiplicity.py)

Run this exercise: `python -m unittest tests.test_count_triplets_target_multiplicity -v`
