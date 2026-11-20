# Count all index pairs with a target sum

Each new value pairs with every earlier occurrence of its complement. Query before inserting so an element cannot pair with itself, and retain frequencies so duplicate values contribute all distinct index pairs.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/count_pair_sums.py)
- [Tests](../tests/test_count_pair_sums.py)

Run this exercise: `python -m unittest tests.test_count_pair_sums -v`
