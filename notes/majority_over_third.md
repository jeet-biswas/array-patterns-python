# Find all values occurring more than one third of the time

At most two values can exceed n/3 occurrences. Cancel triples of distinct candidates to retain two possible winners, then count them in a second pass to reject false candidates. Return verified values in ascending order.

Complexity: O(n) time, O(1) auxiliary space.

- [Implementation](../arrays/majority_over_third.py)
- [Tests](../tests/test_majority_over_third.py)

Run this exercise: `python -m unittest tests.test_majority_over_third -v`
