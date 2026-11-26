# Rank an array among its distinct multiset permutations

Start with the multinomial count of all distinct permutations. At each position, count blocks beginning with smaller remaining values. A value occurring c times owns total*c/remaining permutations. Update that total after consuming the actual value. u is the distinct value count; exact factorial arithmetic has nonconstant bit cost.

Complexity: O(nu + n + u log u) arithmetic operations, O(u) auxiliary slots.

- [Implementation](../arrays/multiset_permutation_rank.py)
- [Tests](../tests/test_multiset_permutation_rank.py)

Run this exercise: `python -m unittest tests.test_multiset_permutation_rank -v`
