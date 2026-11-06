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
| 2 | [Maximum subarray sum](arrays/max_subarray.py) | O(n) time, O(1) space | [Explanation](notes/max_subarray.md) |
| 3 | [Rotate an array in place](arrays/rotate_right.py) | O(n) time, O(1) space | [Explanation](notes/rotate_right.md) |
| 4 | [Move zeros while preserving order](arrays/move_zeros.py) | O(n) time, O(1) space | [Explanation](notes/move_zeros.md) |
| 5 | [Remove duplicates from a sorted array](arrays/compact_sorted.py) | O(n) time, O(1) space | [Explanation](notes/compact_sorted.md) |
| 6 | [Merge two sorted arrays](arrays/merge_sorted.py) | O(n + m) time, O(n + m) output space | [Explanation](notes/merge_sorted.md) |
| 7 | [Product of all other elements](arrays/product_except_self.py) | O(n) arithmetic operations, O(n) output space | [Explanation](notes/product_except_self.md) |
| 8 | [Immutable prefix sums for range queries](arrays/prefix_range_sum.py) | O(n) build/space, O(1) per query | [Explanation](notes/prefix_range_sum.md) |
| 9 | [Verified majority element](arrays/majority_element.py) | O(n) time, O(1) space | [Explanation](notes/majority_element.md) |
| 10 | [Second largest distinct value](arrays/second_largest.py) | O(n) time, O(1) space | [Explanation](notes/second_largest.md) |
| 11 | [Strict leaders from the right](arrays/array_leaders.py) | O(n) time, O(n) output space | [Explanation](notes/array_leaders.md) |
| 12 | [Best single buy/sell profit](arrays/max_stock_profit.py) | O(n) time, O(1) space | [Explanation](notes/max_stock_profit.md) |
| 13 | [Trapping rain water](arrays/trap_rain_water.py) | O(n) time, O(1) space | [Explanation](notes/trap_rain_water.md) |
| 14 | [Longest consecutive value sequence](arrays/longest_consecutive.py) | Expected O(n) time, O(n) space | [Explanation](notes/longest_consecutive.md) |
| 15 | [Count subarrays with a target sum](arrays/count_subarrays_sum.py) | Expected O(n) time, O(n) space | [Explanation](notes/count_subarrays_sum.md) |
| 16 | [Sliding window maximum](arrays/sliding_window_max.py) | O(n) time, O(k) auxiliary space | [Explanation](notes/sliding_window_max.md) |
| 17 | [Sort an array containing 0, 1, and 2](arrays/sort_colors.py) | O(n) time, O(1) space | [Explanation](notes/sort_colors.md) |
| 18 | [Next lexicographic permutation](arrays/next_permutation.py) | O(n) time, O(1) space | [Explanation](notes/next_permutation.md) |
| 19 | [First occurrence binary search](arrays/binary_search.py) | O(log n) time, O(1) space | [Explanation](notes/binary_search.md) |
