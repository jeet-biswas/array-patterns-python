# Best pair score with a distance penalty

Rewrite values[i]+values[j]-(j-i) as (values[i]+i)+(values[j]-j). Before evaluating each right endpoint, keep the best earlier left term; update it afterward so a position cannot pair with itself.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/best_sightseeing_pair.py)
- [Tests](../tests/test_best_sightseeing_pair.py)

Run this exercise: `python -m unittest tests.test_best_sightseeing_pair -v`
