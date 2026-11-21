# Maximum ordered equal-value matches between arrays

Matching equal endpoints extends the diagonal prefix result; otherwise skip either endpoint. Keeping one previous row is enough. The order restriction means the drawn matches never cross.

Complexity: O(nm) time, O(m) space.

- [Implementation](../arrays/max_uncrossed_matches.py)
- [Tests](../tests/test_max_uncrossed_matches.py)

Run this exercise: `python -m unittest tests.test_max_uncrossed_matches -v`
