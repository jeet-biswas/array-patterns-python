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
| 20 | [Container with most water](arrays/max_container_area.py) | O(n) time, O(1) space | [Explanation](notes/max_container_area.md) |
| 21 | [Sorted squares of a sorted array](arrays/sorted_squares.py) | O(n) time, O(n) output space | [Explanation](notes/sorted_squares.md) |
| 22 | [Unique zero-sum triplets](arrays/three_sum.py) | O(n squared) time, O(n) auxiliary space plus output | [Explanation](notes/three_sum.md) |
| 23 | [Maximum product subarray](arrays/max_product_subarray.py) | O(n) arithmetic operations, O(1) space | [Explanation](notes/max_product_subarray.md) |
| 24 | [Shortest subarray reaching a positive target](arrays/min_length_sum.py) | O(n) time, O(1) space | [Explanation](notes/min_length_sum.md) |
| 25 | [Longest subarray with an exact sum](arrays/longest_subarray_sum.py) | Expected O(n) time, O(n) space | [Explanation](notes/longest_subarray_sum.md) |
| 26 | [First equilibrium index](arrays/pivot_index.py) | O(n) time, O(1) space | [Explanation](notes/pivot_index.md) |
| 27 | [Multiset intersection of sorted arrays](arrays/intersect_sorted.py) | O(n + m) time, O(min(n, m)) output space | [Explanation](notes/intersect_sorted.md) |
| 28 | [Kth largest array element](arrays/kth_largest.py) | O(n log(k + 1)) time, O(k) space | [Explanation](notes/kth_largest.md) |
| 29 | [Merge overlapping closed intervals](arrays/merge_intervals.py) | O(n log n) time, O(n) space | [Explanation](notes/merge_intervals.md) |
| 30 | [Smallest missing positive integer](arrays/smallest_missing_positive.py) | O(n) time, O(1) space | [Explanation](notes/smallest_missing_positive.md) |
| 31 | [Maximum circular subarray sum](arrays/max_circular_subarray.py) | O(n) time, O(1) space | [Explanation](notes/max_circular_subarray.md) |
| 32 | [Sum of every subarray minimum](arrays/sum_subarray_minimums.py) | O(n) time, O(n) space | [Explanation](notes/sum_subarray_minimums.md) |
| 33 | [Minimum forward jumps to the last index](arrays/min_jumps.py) | O(n) time, O(1) space | [Explanation](notes/min_jumps.md) |
| 34 | [Count inversions using merge sort](arrays/inversion_count.py) | O(n log n) time, O(n) space | [Explanation](notes/inversion_count.md) |
| 35 | [Search a rotated sorted array](arrays/search_rotated.py) | O(log n) time, O(1) space | [Explanation](notes/search_rotated.md) |
| 36 | [Minimum arbitrary swaps to group ones](arrays/min_swaps_group_ones.py) | O(n) time, O(1) space | [Explanation](notes/min_swaps_group_ones.md) |
| 37 | [Unique quadruplets with a target sum](arrays/four_sum.py) | O(n cubed) time, O(n) auxiliary space plus output | [Explanation](notes/four_sum.md) |
| 38 | [Closest triplet sum with deterministic ties](arrays/three_sum_closest.py) | O(n squared) time, O(n) space | [Explanation](notes/three_sum_closest.md) |
| 39 | [Maximum sum of nonadjacent elements](arrays/max_non_adjacent_sum.py) | O(n) time, O(1) space | [Explanation](notes/max_non_adjacent_sum.md) |
| 40 | [Length of a strictly increasing subsequence](arrays/lis_length.py) | O(n log(n + 1)) time, O(n) space | [Explanation](notes/lis_length.md) |
| 41 | [Count smaller elements to the right](arrays/count_smaller_right.py) | O(n log(n + 1)) time, O(n) space | [Explanation](notes/count_smaller_right.md) |
| 42 | [Next strictly greater element on the right](arrays/next_greater_right.py) | O(n) time, O(n) space | [Explanation](notes/next_greater_right.md) |
| 43 | [Days until a warmer temperature](arrays/daily_temperatures.py) | O(n) time, O(n) space | [Explanation](notes/daily_temperatures.md) |
| 44 | [Largest rectangle in a histogram](arrays/largest_histogram_rectangle.py) | O(n) time, O(n) space | [Explanation](notes/largest_histogram_rectangle.md) |
| 45 | [Maximum width ramp](arrays/max_width_ramp.py) | O(n) time, O(n) space | [Explanation](notes/max_width_ramp.md) |
| 46 | [Shortest window that needs sorting](arrays/shortest_unsorted_window.py) | O(n) time, O(1) space | [Explanation](notes/shortest_unsorted_window.md) |
| 47 | [Count subarrays divisible by a modulus](arrays/count_subarrays_divisible.py) | Expected O(n) time, O(min(n, k)) space | [Explanation](notes/count_subarrays_divisible.md) |
| 48 | [Longest subarray with equal zeros and ones](arrays/longest_balanced_binary.py) | Expected O(n) time, O(n) space | [Explanation](notes/longest_balanced_binary.md) |
| 49 | [Longest ones window after limited flips](arrays/longest_ones_after_flips.py) | O(n) time, O(1) space | [Explanation](notes/longest_ones_after_flips.md) |
| 50 | [Count subarrays with exactly k distinct values](arrays/subarrays_exactly_k_distinct.py) | Expected O(n) time, O(min(n, k)) space | [Explanation](notes/subarrays_exactly_k_distinct.md) |
| 51 | [Shortest qualifying subarray with signed values](arrays/shortest_subarray_signed.py) | O(n) time, O(n) space | [Explanation](notes/shortest_subarray_signed.md) |
| 52 | [Median of two sorted arrays](arrays/median_two_sorted.py) | O(log(min(n, m) + 1)) time, O(1) space | [Explanation](notes/median_two_sorted.md) |
| 53 | [Kth missing positive integer in a sorted array](arrays/kth_missing_positive.py) | O(log(n + 1)) time, O(1) space | [Explanation](notes/kth_missing_positive.md) |
| 54 | [Best sum of two fixed-length disjoint subarrays](arrays/max_sum_two_nonoverlapping.py) | O(n) time, O(n) space | [Explanation](notes/max_sum_two_nonoverlapping.md) |
| 55 | [Apply many range increments with a difference array](arrays/range_additions.py) | O(n + q) time, O(n) space | [Explanation](notes/range_additions.md) |
| 56 | [Best pair score with a distance penalty](arrays/best_sightseeing_pair.py) | O(n) time, O(1) space | [Explanation](notes/best_sightseeing_pair.md) |
| 57 | [Lower and upper bounds in a sorted array](arrays/equal_range.py) | O(log(n + 1)) time, O(1) space | [Explanation](notes/equal_range.md) |
| 58 | [Minimum in a rotated array with duplicates](arrays/find_min_rotated.py) | O(log n) typical, O(n) worst-case time, O(1) space | [Explanation](notes/find_min_rotated.md) |
| 59 | [Find a strict local peak](arrays/peak_index.py) | O(log(n + 1)) time, O(1) space | [Explanation](notes/peak_index.md) |
| 60 | [Duplicate zeros in a fixed-length array](arrays/duplicate_zeros.py) | O(n) time, O(1) space | [Explanation](notes/duplicate_zeros.md) |
| 61 | [Merge sorted arrays into an existing buffer](arrays/merge_into_buffer.py) | O(n + m) time, O(1) space | [Explanation](notes/merge_into_buffer.md) |
| 62 | [Increment a decimal digit array](arrays/plus_one.py) | O(n) time, O(n) output space | [Explanation](notes/plus_one.md) |
| 63 | [Add two decimal digit arrays](arrays/add_digit_arrays.py) | O(n + m) time, O(max(n, m)) output space | [Explanation](notes/add_digit_arrays.md) |
| 64 | [Generate one row of Pascal triangle](arrays/pascal_row.py) | O(n squared) arithmetic operations, O(n) space | [Explanation](notes/pascal_row.md) |
| 65 | [Longest strict mountain subarray](arrays/longest_mountain.py) | O(n) time, O(1) space | [Explanation](notes/longest_mountain.md) |
| 66 | [Smallest ordered prefix-suffix partition](arrays/partition_disjoint.py) | O(n) time, O(1) space | [Explanation](notes/partition_disjoint.md) |
| 67 | [Maximum independently sortable chunks](arrays/max_chunks_sorted.py) | O(n) time, O(n) space | [Explanation](notes/max_chunks_sorted.md) |
| 68 | [Minimum increments to make values unique](arrays/min_increment_unique.py) | O(n log n) time, O(n) space | [Explanation](notes/min_increment_unique.md) |
| 69 | [Minimum unit moves to equalize an array](arrays/min_moves_equal.py) | O(n log n) time, O(n) space | [Explanation](notes/min_moves_equal.md) |
| 70 | [Maximum absolute subarray sum](arrays/max_absolute_subarray.py) | O(n) time, O(1) space | [Explanation](notes/max_absolute_subarray.md) |
| 71 | [Maximum sum strictly increasing subsequence](arrays/max_sum_increasing_subsequence.py) | O(n squared) time, O(n) space | [Explanation](notes/max_sum_increasing_subsequence.md) |
