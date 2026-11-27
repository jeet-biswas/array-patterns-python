# Count distinct permutations whose neighbor sums are perfect squares

Precompute compatible value pairs with integer square roots. Memoize used-index masks and the last chosen index. To avoid counting duplicate value permutations, allow a repeated value only after its preceding equal copy has been used. The empty permutation is counted once. Integer square-root bit costs are additional; use small arrays.

Complexity: O(n squared 2^n) state-transition operations, O(n 2^n + n squared) space.

- [Implementation](../arrays/count_square_sum_permutations.py)
- [Tests](../tests/test_count_square_sum_permutations.py)

Run this exercise: `python -m unittest tests.test_count_square_sum_permutations -v`
