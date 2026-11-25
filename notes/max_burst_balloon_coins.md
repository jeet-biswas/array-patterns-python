# Maximum coins from removing balloons in any order

Pad the array with boundary ones and choose the last balloon removed inside each interval. At that moment its surviving neighbors are the interval boundaries, fixing its reward. The two sides can therefore be optimized independently.

Complexity: O(n cubed) time, O(n squared) space.

- [Implementation](../arrays/max_burst_balloon_coins.py)
- [Tests](../tests/test_max_burst_balloon_coins.py)

Run this exercise: `python -m unittest tests.test_max_burst_balloon_coins -v`
