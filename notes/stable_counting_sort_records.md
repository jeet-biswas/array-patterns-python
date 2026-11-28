# Stably sort integer-key records with bounded keys

Count each key, convert frequencies into starting output positions, and place records in their input order. Advancing each key's next position preserves payload order among equal keys. The caller supplies the key range, making memory use explicit.

Complexity: O(n + k) time, O(n + k) space.

- [Implementation](../arrays/stable_counting_sort_records.py)
- [Tests](../tests/test_stable_counting_sort_records.py)

Run this exercise: `python -m unittest tests.test_stable_counting_sort_records -v`
