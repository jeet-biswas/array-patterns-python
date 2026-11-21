# Fewest replacements to obtain consecutive distinct values

A valid final array of length n contains n distinct consecutive integers in any order. Sort and deduplicate the input, then keep the largest window whose span is below n. All remaining positions must be replaced, including duplicates.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/min_replacements_continuous.py)
- [Tests](../tests/test_min_replacements_continuous.py)

Run this exercise: `python -m unittest tests.test_min_replacements_continuous -v`
