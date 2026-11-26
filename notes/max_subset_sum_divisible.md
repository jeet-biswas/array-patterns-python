# Maximum signed subset sum divisible by a chosen modulus

Keep the greatest reachable sum for each remainder. Copy each DP layer before considering a value so it is used at most once. None denotes an unreachable remainder; negative intermediate sums may enable a later optimum. m is the modulus.

Complexity: O(nm) time, O(m) space.

- [Implementation](../arrays/max_subset_sum_divisible.py)
- [Tests](../tests/test_max_subset_sum_divisible.py)

Run this exercise: `python -m unittest tests.test_max_subset_sum_divisible -v`
