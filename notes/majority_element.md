# Verified majority element

Boyer-Moore voting cancels pairs of unequal values. A second pass verifies that the surviving candidate occurs strictly more than half the time; a majority is not assumed to exist.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/majority_element.py)
- [Tests](../tests/test_majority_element.py)

Run this exercise: `python -m unittest tests.test_majority_element -v`
