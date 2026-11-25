# Longest chain of strictly separated interval pairs

Sort intervals by their ending value and repeatedly select the earliest finish strictly beyond the previously selected end. Replacing a chosen interval by an earlier-finishing eligible interval never reduces future choices. Input pairs may be reordered.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/longest_interval_chain.py)
- [Tests](../tests/test_longest_interval_chain.py)

Run this exercise: `python -m unittest tests.test_longest_interval_chain -v`
