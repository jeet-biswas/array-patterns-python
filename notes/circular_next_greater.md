# Next greater values in a circular array

Scan a virtual doubled array backwards, maintaining a decreasing stack of candidates. The first virtual pass supplies wraparound candidates; record answers only for original positions. Strict comparison excludes equal values and self-matches.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/circular_next_greater.py)
- [Tests](../tests/test_circular_next_greater.py)

Run this exercise: `python -m unittest tests.test_circular_next_greater -v`
