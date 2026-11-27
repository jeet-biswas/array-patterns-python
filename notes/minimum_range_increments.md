# Build a nonnegative target using unit subarray increments

Every increase above the preceding height requires that many new interval operations to start. When height falls, existing operations can simply end. The sum of positive rises from an initial height zero is both a lower bound and achievable.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/minimum_range_increments.py)
- [Tests](../tests/test_minimum_range_increments.py)

Run this exercise: `python -m unittest tests.test_minimum_range_increments -v`
