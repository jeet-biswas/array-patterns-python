# Count distinct nonempty value subsequences

Maintain the count including the empty sequence. Appending the current value doubles it, but subsequences already created at the previous occurrence would be duplicated. Subtract the total that existed immediately before that previous occurrence. Counts are exact big integers, whose arithmetic cost grows with their width.

Complexity: Expected O(n) arithmetic operations, O(n) auxiliary slots.

- [Implementation](../arrays/count_distinct_value_subsequences.py)
- [Tests](../tests/test_count_distinct_value_subsequences.py)

Run this exercise: `python -m unittest tests.test_count_distinct_value_subsequences -v`
