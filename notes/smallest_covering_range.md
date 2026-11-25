# Smallest value range covering every sorted input array

Keep one current value from each sorted array in a min-heap and track their maximum. The current minimum-to-maximum interval covers every array. Advance the array supplying the minimum; no interval with that same minimum can improve by increasing another value. N is total input length, k is the array count.

Complexity: O(N + N log(k + 1)) time, O(k) space.

- [Implementation](../arrays/smallest_covering_range.py)
- [Tests](../tests/test_smallest_covering_range.py)

Run this exercise: `python -m unittest tests.test_smallest_covering_range -v`
