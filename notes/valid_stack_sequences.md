# Validate paired push and pop arrays

Push values in their fixed order, immediately popping whenever the top matches the next desired output. For distinct pushed values a requested pop uniquely identifies its item, so delaying an available pop cannot unlock another valid order. Duplicate pushed values are explicitly rejected.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/valid_stack_sequences.py)
- [Tests](../tests/test_valid_stack_sequences.py)

Run this exercise: `python -m unittest tests.test_valid_stack_sequences -v`
