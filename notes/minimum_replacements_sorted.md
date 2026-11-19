# Minimum splits to make an array nondecreasing

Scan from the right with the largest allowed next value. Split an oversized element into the fewest positive parts fitting that bound, then balance those parts to maximize the smallest resulting part, preserving flexibility for earlier elements.

Complexity: O(n) arithmetic operations, O(1) space.

- [Implementation](../arrays/minimum_replacements_sorted.py)
- [Tests](../tests/test_minimum_replacements_sorted.py)

Run this exercise: `python -m unittest tests.test_minimum_replacements_sorted -v`
