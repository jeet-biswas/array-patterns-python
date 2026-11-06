# Two sum

Store previously seen values and their earliest indices. Look up the complement before inserting the current value, so an element is never reused.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/two_sum.py)
- [Tests](../tests/test_two_sum.py)

Run this exercise: `python -m unittest tests.test_two_sum -v`
