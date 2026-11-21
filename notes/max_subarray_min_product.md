# Maximum subarray sum times its minimum

Prefix sums give interval sums. A monotone stack identifies the widest interval where each element can serve as its minimum. Nonnegative values make the widest such interval optimal. Equal minima are resolved by popping the earlier index.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/max_subarray_min_product.py)
- [Tests](../tests/test_max_subarray_min_product.py)

Run this exercise: `python -m unittest tests.test_max_subarray_min_product -v`
