# Minimum cross-array swap cost to equalize two multisets

Frequency differences must be even. Build the surplus values on each side and pair the smallest on one side with the largest on the other. Each pair can be exchanged directly at the cheaper value, or indirectly through the global minimum twice. The intermediate minimum is restored after the two swaps.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/minimum_basket_swap_cost.py)
- [Tests](../tests/test_minimum_basket_swap_cost.py)

Run this exercise: `python -m unittest tests.test_minimum_basket_swap_cost -v`
