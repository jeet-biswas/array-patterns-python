# Count pairs with a greater-than-double relation

Sort halves recursively, then count cross-half pairs using a monotonic right pointer before merging. The comparison values[i] > 2*values[j] must be performed separately from the ordinary merge comparison, especially for negative numbers.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/count_reverse_pairs.py)
- [Tests](../tests/test_count_reverse_pairs.py)

Run this exercise: `python -m unittest tests.test_count_reverse_pairs -v`
