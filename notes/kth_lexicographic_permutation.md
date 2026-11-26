# Select a ranked permutation of distinct array values

Sort values and decompose the zero-based rank using factorial block sizes. Each leading choice owns (remaining-minus-one) factorial permutations. Remove the selected value and repeat for the remainder. Python list removals are linear and factorial arithmetic uses big integers.

Complexity: O(n squared) arithmetic/list operations, O(n) auxiliary slots.

- [Implementation](../arrays/kth_lexicographic_permutation.py)
- [Tests](../tests/test_kth_lexicographic_permutation.py)

Run this exercise: `python -m unittest tests.test_kth_lexicographic_permutation -v`
