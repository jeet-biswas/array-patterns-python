# Maximum nesting chain of width-height pairs

Sort by increasing width and decreasing height for equal widths. A strict increasing subsequence of heights then enforces both dimensions: the reversed tie order prevents selecting two equal-width envelopes. Rotation is not permitted.

Complexity: O(n log(n + 1)) time, O(n) space.

- [Implementation](../arrays/maximum_envelope_nesting.py)
- [Tests](../tests/test_maximum_envelope_nesting.py)

Run this exercise: `python -m unittest tests.test_maximum_envelope_nesting -v`
