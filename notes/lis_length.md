# Length of a strictly increasing subsequence

Maintain the smallest tail value for each attainable subsequence length. Lower-bound replacement keeps future extension opportunities open; equal values replace rather than extend a tail.

Complexity: O(n log(n + 1)) time, O(n) space.

- [Implementation](../arrays/lis_length.py)
- [Tests](../tests/test_lis_length.py)

Run this exercise: `python -m unittest tests.test_lis_length -v`
