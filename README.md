# Array patterns in Python

An array-only study collection: small implementations, explicit edge-case behavior,
complexity notes, and deterministic tests. Written with AI assistance and checked
against examples and independent reference approaches. No third-party packages.

## Run

Requires Python 3.10 or newer. From the repository root:

```sh
python -m unittest discover -s tests -v
```

Tests cover normal cases, boundaries, invalid inputs where specified, and
fixed-seed comparisons against simple reference solutions. This is learning code;
functions assume integer array elements. Sorted-input preconditions are documented
and deliberately not checked so logarithmic or constant-space bounds are retained.
Complexity uses the usual unit-cost arithmetic model unless a note says otherwise.

Functions document whether they mutate their input. `compact_sorted` returns the
length of a unique prefix; its remaining tail is unspecified. Range queries use
half-open intervals. See each implementation for its exact contract.

## Exercises

| # | Problem | Complexity | Notes |
|---|---|---|---|
| 1 | [Two sum](arrays/two_sum.py) | O(n) time, O(n) space | [Explanation](notes/two_sum.md) |
