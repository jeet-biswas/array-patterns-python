# Sort signed integers with stable byte-wise radix passes

Subtract the smallest value to obtain nonnegative keys without changing their order. Stable counting passes process one byte at a time from least significant to most significant. B is the byte width of the value range; large-integer shifts have additional bit costs.

Complexity: O((n + 256)B) digit operations, O(n + 256) space.

- [Implementation](../arrays/signed_radix_sort.py)
- [Tests](../tests/test_signed_radix_sort.py)

Run this exercise: `python -m unittest tests.test_signed_radix_sort -v`
