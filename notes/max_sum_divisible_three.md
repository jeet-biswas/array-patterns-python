# Maximum subset sum divisible by three

Keep the best attainable sum for each of three remainders. For each value, update from a snapshot so it is used at most once. None marks unreachable states, while the empty subset supplies remainder zero.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/max_sum_divisible_three.py)
- [Tests](../tests/test_max_sum_divisible_three.py)

Run this exercise: `python -m unittest tests.test_max_sum_divisible_three -v`
