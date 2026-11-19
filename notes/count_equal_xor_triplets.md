# Count splits with equal left and right XOR

Equal XOR on the two sides means equal prefix XOR at the whole segment boundaries. If previous matching positions are p, each contributes stop-p-1 valid split points. Store their count and sum to aggregate these contributions in constant hash operations.

Complexity: Expected O(n) hash operations, O(n) space.

- [Implementation](../arrays/count_equal_xor_triplets.py)
- [Tests](../tests/test_count_equal_xor_triplets.py)

Run this exercise: `python -m unittest tests.test_count_equal_xor_triplets -v`
