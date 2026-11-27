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
| 72 | [Count longest increasing subsequences](arrays/count_lis.py) | O(n squared) time, O(n) space | [Explanation](notes/count_lis.md) |
| 73 | [Longest arithmetic subsequence](arrays/longest_arithmetic_subsequence.py) | Expected O(n squared) time, O(n squared) space | [Explanation](notes/longest_arithmetic_subsequence.md) |
| 74 | [Count contiguous arithmetic slices](arrays/arithmetic_slices.py) | O(n) time, O(1) space | [Explanation](notes/arithmetic_slices.md) |
| 75 | [Maximum subset sum divisible by three](arrays/max_sum_divisible_three.py) | O(n) time, O(1) space | [Explanation](notes/max_sum_divisible_three.md) |
| 76 | [Minimize the largest contiguous partition sum](arrays/split_array_min_largest_sum.py) | O(n log(S + 1)) time, O(1) space | [Explanation](notes/split_array_min_largest_sum.md) |
| 77 | [Maximize minimum distance between selected positions](arrays/max_min_distance.py) | O(n log n + n log(D + 1)) time, O(n) space | [Explanation](notes/max_min_distance.md) |
| 78 | [Partition an array into equal-sum subsets](arrays/can_partition_equal_subset.py) | O(nT) time, O(T) space | [Explanation](notes/can_partition_equal_subset.md) |
| 79 | [Count subsets with a target sum](arrays/subset_sum_count.py) | Expected O(nR) time, O(R) space | [Explanation](notes/subset_sum_count.md) |
| 80 | [Maximum subarray sum with at most one deletion](arrays/max_subarray_one_deletion.py) | O(n) time, O(1) space | [Explanation](notes/max_subarray_one_deletion.md) |
| 81 | [Maximum stock profit with a one-day cooldown](arrays/max_profit_cooldown.py) | O(n) time, O(1) space | [Explanation](notes/max_profit_cooldown.md) |
| 82 | [Count pairs with a greater-than-double relation](arrays/count_reverse_pairs.py) | O(n log n) time, O(n) space | [Explanation](notes/count_reverse_pairs.md) |
| 83 | [Count valid triangle triplets](arrays/triangle_count.py) | O(n squared) time, O(n) space | [Explanation](notes/triangle_count.md) |
| 84 | [Count subarrays with product below a threshold](arrays/count_product_below.py) | O(n) arithmetic operations, O(1) space | [Explanation](notes/count_product_below.md) |
| 85 | [Count subarrays with maximum in an interval](arrays/count_bounded_max.py) | O(n) time, O(1) space | [Explanation](notes/count_bounded_max.md) |
| 86 | [Count subarrays with exact minimum and maximum](arrays/count_fixed_bounds.py) | O(n) time, O(1) space | [Explanation](notes/count_fixed_bounds.md) |
| 87 | [Maximum frequency after limited increments](arrays/max_frequency_increments.py) | O(n log n) time, O(n) space | [Explanation](notes/max_frequency_increments.md) |
| 88 | [Shortest removal making the remaining sum divisible](arrays/min_removal_divisible.py) | Expected O(n) time, O(min(n, p)) space | [Explanation](notes/min_removal_divisible.md) |
| 89 | [Minimum end removals with a target sum](arrays/min_end_removals_sum.py) | Expected O(n) time, O(n) space | [Explanation](notes/min_end_removals_sum.md) |
| 90 | [Minimum arbitrary swaps to sort a permutation](arrays/min_swaps_permutation.py) | O(n) time, O(n) space | [Explanation](notes/min_swaps_permutation.md) |
| 91 | [Maximum index-weighted rotation score](arrays/max_rotation_score.py) | O(n) time, O(1) space | [Explanation](notes/max_rotation_score.md) |
| 92 | [Next greater values in a circular array](arrays/circular_next_greater.py) | O(n) time, O(n) space | [Explanation](notes/circular_next_greater.md) |
| 93 | [Resolve one-dimensional asteroid collisions](arrays/asteroid_collision.py) | O(n) time, O(n) space | [Explanation](notes/asteroid_collision.md) |
| 94 | [Apply the first eligible future price discount](arrays/final_discount_prices.py) | O(n) time, O(n) space | [Explanation](notes/final_discount_prices.md) |
| 95 | [Compute consecutive backward stock spans](arrays/stock_spans.py) | O(n) time, O(n) space | [Explanation](notes/stock_spans.md) |
| 96 | [Sum of all contiguous subarray ranges](arrays/sum_subarray_ranges.py) | O(n) time, O(n) space | [Explanation](notes/sum_subarray_ranges.md) |
| 97 | [Maximum subarray sum with a divisible length](arrays/max_sum_length_multiple.py) | Expected O(n) time, O(min(n, k)) space | [Explanation](notes/max_sum_length_multiple.md) |
| 98 | [Minimum adjacent swaps to group all ones](arrays/min_adjacent_swaps_ones.py) | O(n) time, O(n) space | [Explanation](notes/min_adjacent_swaps_ones.md) |
| 99 | [Minimum candies respecting adjacent ratings](arrays/minimum_candy.py) | O(n) time, O(n) space | [Explanation](notes/minimum_candy.md) |
| 100 | [Find a feasible circular gas-station start](arrays/gas_station_start.py) | O(n) time, O(1) space | [Explanation](notes/gas_station_start.md) |
| 101 | [Longest alternating-difference subsequence](arrays/wiggle_subsequence_length.py) | O(n) time, O(1) space | [Explanation](notes/wiggle_subsequence_length.md) |
| 102 | [Longest window with bounded value spread](arrays/longest_subarray_limit.py) | O(n) time, O(n) space | [Explanation](notes/longest_subarray_limit.md) |
| 103 | [Medians of consecutive fixed-size windows](arrays/sliding_window_medians.py) | O(nk + k log k) time, O(k) auxiliary space | [Explanation](notes/sliding_window_medians.md) |
| 104 | [Count subarray sums inside an inclusive range](arrays/count_range_sums.py) | O(n log n) time, O(n) space | [Explanation](notes/count_range_sums.md) |
| 105 | [Count subarrays with a target XOR](arrays/count_subarrays_xor.py) | Expected O(n) time, O(n) space | [Explanation](notes/count_subarrays_xor.md) |
| 106 | [Maximum XOR of two array elements](arrays/max_xor_pair.py) | O(nB) time, O(nB) space | [Explanation](notes/max_xor_pair.md) |
| 107 | [Static half-open range XOR queries](arrays/xor_range_query.py) | O(n) build/space, O(1) query operations | [Explanation](notes/xor_range_query.md) |
| 108 | [Shortest subarray meeting a bitwise OR threshold](arrays/shortest_subarray_or.py) | O(nB) time, O(B) auxiliary space | [Explanation](notes/shortest_subarray_or.md) |
| 109 | [Count distinct OR results of all subarrays](arrays/count_distinct_subarray_ors.py) | Expected O(nB) set operations, O(nB) space | [Explanation](notes/count_distinct_subarray_ors.md) |
| 110 | [Maximum bitwise AND of two elements](arrays/max_and_pair.py) | O(nB) bit checks, O(1) auxiliary slots | [Explanation](notes/max_and_pair.md) |
| 111 | [Count splits with equal left and right XOR](arrays/count_equal_xor_triplets.py) | Expected O(n) hash operations, O(n) space | [Explanation](notes/count_equal_xor_triplets.md) |
| 112 | [Sum of all odd-length subarrays](arrays/sum_odd_length_subarrays.py) | O(n) time, O(1) space | [Explanation](notes/sum_odd_length_subarrays.md) |
| 113 | [Range sums with position-relative weights](arrays/weighted_range_sum.py) | O(n) build/space, O(1) per query | [Explanation](notes/weighted_range_sum.md) |
| 114 | [Static range minimum sparse table](arrays/range_min_table.py) | O(n log(n + 1)) build/space, O(1) queries | [Explanation](notes/range_min_table.md) |
| 115 | [Mutable range sums with a Fenwick array](arrays/fenwick_range_sum.py) | O(n) build/space, O(log(n + 1)) updates and queries | [Explanation](notes/fenwick_range_sum.md) |
| 116 | [Batch distinct-value counts for array ranges](arrays/offline_distinct_queries.py) | Expected O((n + q) log(n + 2)) time, O(n + q) space | [Explanation](notes/offline_distinct_queries.md) |
| 117 | [Kth smallest absolute pair distance](arrays/kth_pair_distance.py) | O(n log n + n log(D + 1)) time, O(n) space | [Explanation](notes/kth_pair_distance.md) |
| 118 | [Enumerate the smallest pairs from two sorted arrays](arrays/smallest_pair_sums.py) | O(r + t log(r + 1)) time, O(r) space plus output | [Explanation](notes/smallest_pair_sums.md) |
| 119 | [Equalize array values with per-element costs](arrays/min_cost_equal_weighted.py) | O(n log n) time, O(n) space | [Explanation](notes/min_cost_equal_weighted.md) |
| 120 | [Maximum score from exactly k end picks](arrays/max_points_from_ends.py) | O(k) time, O(1) space | [Explanation](notes/max_points_from_ends.md) |
| 121 | [Minimum splits to make an array nondecreasing](arrays/minimum_replacements_sorted.py) | O(n) arithmetic operations, O(1) space | [Explanation](notes/minimum_replacements_sorted.md) |
| 122 | [Median after each array prefix](arrays/running_medians.py) | O(n log(n + 1)) time, O(n) space | [Explanation](notes/running_medians.md) |
| 123 | [Best three disjoint fixed-length windows](arrays/max_sum_three_windows.py) | O(n) time, O(n) space | [Explanation](notes/max_sum_three_windows.md) |
| 124 | [Maximum sum of exactly k equal-width windows](arrays/max_sum_k_windows.py) | O(nk) time, O(n) space | [Explanation](notes/max_sum_k_windows.md) |
| 125 | [Stock profit with a transaction limit](arrays/max_profit_transactions.py) | O(n min(k, n)) time, O(min(k, n)) space | [Explanation](notes/max_profit_transactions.md) |
| 126 | [Stock profit with a fee per completed trade](arrays/max_profit_fee.py) | O(n) time, O(1) space | [Explanation](notes/max_profit_fee.md) |
| 127 | [Longest alternating contiguous comparison run](arrays/longest_turbulent_subarray.py) | O(n) time, O(1) space | [Explanation](notes/longest_turbulent_subarray.md) |
| 128 | [Count contiguous subarrays with odd sum](arrays/count_odd_sum_subarrays.py) | O(n) time, O(1) space | [Explanation](notes/count_odd_sum_subarrays.md) |
| 129 | [Count equal-value index pairs](arrays/count_equal_pairs.py) | Expected O(n) time, O(n) space | [Explanation](notes/count_equal_pairs.md) |
| 130 | [Count pairs violating the index-value difference rule](arrays/count_bad_pairs.py) | Expected O(n) time, O(n) space | [Explanation](notes/count_bad_pairs.md) |
| 131 | [Count index pairs with a fixed absolute difference](arrays/count_pairs_difference.py) | Expected O(n) time, O(n) space | [Explanation](notes/count_pairs_difference.md) |
| 132 | [Count all index pairs with a target sum](arrays/count_pair_sums.py) | Expected O(n) time, O(n) space | [Explanation](notes/count_pair_sums.md) |
| 133 | [Count pairs below a strict sum threshold](arrays/count_pairs_below_sum.py) | O(n log n) time, O(n) space | [Explanation](notes/count_pairs_below_sum.md) |
| 134 | [Count subsequences with bounded minimum-plus-maximum](arrays/count_subsequences_minmax.py) | O(n log n) comparisons, O(n) auxiliary slots | [Explanation](notes/count_subsequences_minmax.md) |
| 135 | [Sum widths of all nonempty subsequences](arrays/sum_subsequence_widths.py) | O(n log n) comparisons, O(n) auxiliary slots | [Explanation](notes/sum_subsequence_widths.md) |
| 136 | [Choose paired indices for maximum sum-times-minimum](arrays/max_subsequence_score.py) | O(n log n + n log(k + 1)) time, O(n + k) space | [Explanation](notes/max_subsequence_score.md) |
| 137 | [Minimum time for parallel workers to finish trips](arrays/min_total_trip_time.py) | O(n log(T + 1)) time, O(1) space | [Explanation](notes/min_total_trip_time.md) |
| 138 | [Earliest day for disjoint adjacent bouquets](arrays/min_bouquet_day.py) | O(n log(D + 1)) time, O(1) space | [Explanation](notes/min_bouquet_day.md) |
| 139 | [Count products meeting a threshold for each query value](arrays/successful_product_pairs.py) | O(m log m + n log(m + 1)) time, O(n + m) space | [Explanation](notes/successful_product_pairs.md) |
| 140 | [Minimize paired absolute differences with one replacement](arrays/min_absolute_sum_difference.py) | O(n log n) time, O(n) space | [Explanation](notes/min_absolute_sum_difference.md) |
| 141 | [Minimum range after at most three value changes](arrays/minimum_range_three_changes.py) | O(n log n) time, O(n) space | [Explanation](notes/minimum_range_three_changes.md) |
| 142 | [Count all-zero contiguous subarrays](arrays/zero_filled_subarrays.py) | O(n) time, O(1) space | [Explanation](notes/zero_filled_subarrays.md) |
| 143 | [Longest subarray with positive product](arrays/longest_positive_product.py) | O(n) time, O(1) space | [Explanation](notes/longest_positive_product.md) |
| 144 | [Maximum alternating signed subsequence sum](arrays/max_alternating_subsequence_sum.py) | O(n) time, O(1) space | [Explanation](notes/max_alternating_subsequence_sum.md) |
| 145 | [Best sum after replacing blocks by their maxima](arrays/partition_max_sum.py) | O(nk) time, O(n) space | [Explanation](notes/partition_max_sum.md) |
| 146 | [Maximum score when adjacent values are forbidden](arrays/delete_and_earn.py) | O(n + u log u) time, O(u) space | [Explanation](notes/delete_and_earn.md) |
| 147 | [Maximum nonadjacent sum on a circular array](arrays/max_circular_nonadjacent_sum.py) | O(n) time, O(1) auxiliary space | [Explanation](notes/max_circular_nonadjacent_sum.md) |
| 148 | [Minimum cost to climb an array of steps](arrays/min_climbing_cost.py) | O(n) time, O(1) space | [Explanation](notes/min_climbing_cost.md) |
| 149 | [Maximum score with bounded forward jumps](arrays/max_jump_score.py) | O(n) time, O(n) space | [Explanation](notes/max_jump_score.md) |
| 150 | [Maximum subsequence sum with bounded index gaps](arrays/constrained_subsequence_sum.py) | O(n) time, O(min(n, k)) auxiliary space | [Explanation](notes/constrained_subsequence_sum.md) |
| 151 | [Shortest contiguous removal leaving a sorted array](arrays/shortest_removal_sorted.py) | O(n) time, O(1) space | [Explanation](notes/shortest_removal_sorted.md) |
| 152 | [Maximum subarray sum times its minimum](arrays/max_subarray_min_product.py) | O(n) time, O(n) space | [Explanation](notes/max_subarray_min_product.md) |
| 153 | [Largest minimum-times-length score containing an index](arrays/max_score_containing_index.py) | O(n) time, O(n) space | [Explanation](notes/max_score_containing_index.md) |
| 154 | [Count subarrays containing enough equal-value pairs](arrays/count_subarrays_pair_threshold.py) | Expected O(n) time, O(n) space | [Explanation](notes/count_subarrays_pair_threshold.md) |
| 155 | [Count windows containing every distinct array value](arrays/count_complete_subarrays.py) | Expected O(n) time, O(n) space | [Explanation](notes/count_complete_subarrays.md) |
| 156 | [Count all windows with a bounded value spread](arrays/count_bounded_spread_subarrays.py) | O(n) time, O(n) space | [Explanation](notes/count_bounded_spread_subarrays.md) |
| 157 | [Count strictly increasing contiguous subarrays](arrays/count_increasing_subarrays.py) | O(n) time, O(1) space | [Explanation](notes/count_increasing_subarrays.md) |
| 158 | [Count contiguous alternating binary windows](arrays/count_alternating_binary_subarrays.py) | O(n) time, O(1) space | [Explanation](notes/count_alternating_binary_subarrays.md) |
| 159 | [Longest subsequence with a specified difference](arrays/longest_fixed_difference_subsequence.py) | Expected O(n) time, O(n) space | [Explanation](notes/longest_fixed_difference_subsequence.md) |
| 160 | [Count arithmetic subsequences of length at least three](arrays/count_arithmetic_subsequences.py) | Expected O(n squared) time, O(n squared) space | [Explanation](notes/count_arithmetic_subsequences.md) |
| 161 | [Maximum dot product of two nonempty subsequences](arrays/max_subsequence_dot_product.py) | O(nm) time, O(m) space | [Explanation](notes/max_subsequence_dot_product.md) |
| 162 | [Maximum ordered equal-value matches between arrays](arrays/max_uncrossed_matches.py) | O(nm) time, O(m) space | [Explanation](notes/max_uncrossed_matches.md) |
| 163 | [Longest contiguous block shared by two arrays](arrays/longest_common_subarray.py) | O(nm) time, O(m) space | [Explanation](notes/longest_common_subarray.md) |
| 164 | [Insert the fewest values to embed a distinct target](arrays/min_insertions_target_subsequence.py) | O(n + m log(n + 1)) time, O(n) space | [Explanation](notes/min_insertions_target_subsequence.md) |
| 165 | [Fewest replacements to obtain consecutive distinct values](arrays/min_replacements_continuous.py) | O(n log n) time, O(n) space | [Explanation](notes/min_replacements_continuous.md) |
| 166 | [Recover a nonnegative array from shuffled values and doubles](arrays/recover_doubled_array.py) | O(n log n) time, O(n) space | [Explanation](notes/recover_doubled_array.md) |
| 167 | [Pair a signed array into value-and-double pairs](arrays/can_pair_doubles.py) | O(n + u log u) time, O(u) space | [Explanation](notes/can_pair_doubles.md) |
| 168 | [Check whether every inversion is between neighbors](arrays/only_local_inversions.py) | O(n) time, O(1) space | [Explanation](notes/only_local_inversions.md) |
| 169 | [Detect a strict 132 pattern in an array](arrays/has_132_pattern.py) | O(n) time, O(n) space | [Explanation](notes/has_132_pattern.md) |
| 170 | [Validate paired push and pop arrays](arrays/valid_stack_sequences.py) | O(n) time, O(n) space | [Explanation](notes/valid_stack_sequences.md) |
| 171 | [Count visible people to the right by height](arrays/visible_people_right.py) | O(n) time, O(n) space | [Explanation](notes/visible_people_right.md) |
| 172 | [Fewest points needed to hit all closed intervals](arrays/minimum_interval_arrows.py) | O(n log n) time, O(n) space | [Explanation](notes/minimum_interval_arrows.md) |
| 173 | [Fewest removals to make half-open intervals disjoint](arrays/minimum_interval_removals.py) | O(n log n) time, O(n) space | [Explanation](notes/minimum_interval_removals.md) |
| 174 | [Intersect two sorted disjoint interval arrays](arrays/intersect_interval_arrays.py) | O(n + m) time, O(n + m) output space | [Explanation](notes/intersect_interval_arrays.md) |
| 175 | [Insert and merge one closed interval into a sorted array](arrays/insert_closed_interval.py) | O(n) time, O(n) output space | [Explanation](notes/insert_closed_interval.md) |
| 176 | [Attend the most events with one event per integer day](arrays/max_attendable_events.py) | O(n log n) time, O(n) space | [Explanation](notes/max_attendable_events.md) |
| 177 | [Check vehicle capacity across trip intervals](arrays/car_pooling_feasible.py) | O(n log n) time, O(n) space | [Explanation](notes/car_pooling_feasible.md) |
| 178 | [Minimum scheduling slots for repeated tasks with cooldown](arrays/least_task_intervals.py) | Expected O(n) time, O(u) space | [Explanation](notes/least_task_intervals.md) |
| 179 | [Fewest distinct values after exactly k deletions](arrays/least_unique_after_removals.py) | O(n + u log u) time, O(u) space | [Explanation](notes/least_unique_after_removals.md) |
| 180 | [Select and order values for the largest time-weighted sum](arrays/max_time_weighted_satisfaction.py) | O(n log n) time, O(n) space | [Explanation](notes/max_time_weighted_satisfaction.md) |
| 181 | [Fewest patches to cover every subset sum up to a target](arrays/minimum_coverage_patches.py) | O(n + log(target + 1)) time, O(1) auxiliary space | [Explanation](notes/minimum_coverage_patches.md) |
| 182 | [Fewest fixed-length bit flips to obtain all ones](arrays/minimum_k_bit_flips.py) | O(n) time, O(n) space | [Explanation](notes/minimum_k_bit_flips.md) |
| 183 | [Longest window whose elements share no set bits](arrays/longest_disjoint_bit_window.py) | O(n) bitwise operations, O(1) auxiliary slots | [Explanation](notes/longest_disjoint_bit_window.md) |
| 184 | [Largest sum of a fixed-size window with distinct values](arrays/max_distinct_window_sum.py) | Expected O(n) time, O(min(n, k)) space | [Explanation](notes/max_distinct_window_sum.md) |
| 185 | [Largest sum of a duplicate-free contiguous window](arrays/max_unique_subarray_sum.py) | Expected O(n) time, O(n) space | [Explanation](notes/max_unique_subarray_sum.md) |
| 186 | [Count subarrays containing the global maximum at least k times](arrays/count_global_max_occurrences.py) | O(n) time, O(1) space | [Explanation](notes/count_global_max_occurrences.md) |
| 187 | [Longest equal-value block after limited deletions](arrays/longest_equal_after_deletions.py) | Expected O(n) time, O(n) space | [Explanation](notes/longest_equal_after_deletions.md) |
| 188 | [Fewest arbitrary swaps to group ones around a circle](arrays/min_circular_swaps_group_ones.py) | O(n) time, O(1) space | [Explanation](notes/min_circular_swaps_group_ones.md) |
| 189 | [Kth smallest sum among all nonempty subarrays](arrays/kth_smallest_subarray_sum.py) | O(n log(S + 1)) time, O(1) space | [Explanation](notes/kth_smallest_subarray_sum.md) |
| 190 | [Maximum subarray sum with length inside a range](arrays/max_sum_length_range.py) | O(n) time, O(n) space | [Explanation](notes/max_sum_length_range.md) |
| 191 | [Count subarrays with a specified greatest common divisor](arrays/count_subarray_gcd.py) | O(n log(M + 1)) GCD operations, O(log(M + 1)) states | [Explanation](notes/count_subarray_gcd.md) |
| 192 | [Count subarrays with a specified least common multiple](arrays/count_subarray_lcm.py) | O(n log(target + 1)) LCM operations, O(log(target + 1)) states | [Explanation](notes/count_subarray_lcm.md) |
| 193 | [Recover a largest pairwise-divisible subset](arrays/largest_divisible_subset.py) | O(n squared) time, O(n) space | [Explanation](notes/largest_divisible_subset.md) |
| 194 | [Pair all elements so each pair sum is divisible](arrays/can_pair_divisible_sums.py) | Expected O(n) time, O(min(n, modulus)) space | [Explanation](notes/can_pair_divisible_sums.md) |
| 195 | [Fewest deletions to form a strict mountain subsequence](arrays/minimum_mountain_removals.py) | O(n log(n + 1)) time, O(n) space | [Explanation](notes/minimum_mountain_removals.md) |
| 196 | [Longest subsequence with an exact signed sum](arrays/longest_subsequence_target_sum.py) | Expected O(nR) time, O(R) space | [Explanation](notes/longest_subsequence_target_sum.md) |
| 197 | [Maximum value from at most k nonoverlapping events](arrays/max_value_k_events.py) | O(n log n + nk) time, O(n) space | [Explanation](notes/max_value_k_events.md) |
| 198 | [Fewest fuel stops needed to reach a destination](arrays/minimum_refuel_stops.py) | O(n log(n + 1)) time, O(n) space | [Explanation](notes/minimum_refuel_stops.md) |
| 199 | [Furthest array position reachable with bricks and ladders](arrays/furthest_reachable_building.py) | O(n log(min(n, L) + 2)) time, O(min(n, L) + 1) space | [Explanation](notes/furthest_reachable_building.md) |
| 200 | [Hire from both array ends with a limited candidate pool](arrays/total_hiring_cost.py) | O(n + (c + k) log(c + 1)) time, O(c) space | [Explanation](notes/total_hiring_cost.md) |
| 201 | [Minimum total cost of merging array weights in pairs](arrays/minimum_merge_cost.py) | O(n log(n + 1)) time, O(n) space | [Explanation](notes/minimum_merge_cost.md) |
| 202 | [Maximize capital by selecting affordable projects](arrays/maximize_project_capital.py) | O(n log n + k log(n + 1)) time, O(n) space | [Explanation](notes/maximize_project_capital.md) |
| 203 | [Sum absolute differences from each sorted array value](arrays/sum_absolute_differences_sorted.py) | O(n) time, O(n) output space | [Explanation](notes/sum_absolute_differences_sorted.md) |
| 204 | [Sum distances to matching values at every index](arrays/equal_value_index_distances.py) | Expected O(n) time, O(n) space | [Explanation](notes/equal_value_index_distances.md) |
| 205 | [Count subarray deletions leaving a strictly increasing array](arrays/count_increasing_remainder_removals.py) | O(n) time, O(1) space | [Explanation](notes/count_increasing_remainder_removals.md) |
| 206 | [Minimum cutting cost for an array of cut positions](arrays/minimum_stick_cut_cost.py) | O(m cubed) time, O(m squared) space | [Explanation](notes/minimum_stick_cut_cost.md) |
| 207 | [Longest chain of strictly separated interval pairs](arrays/longest_interval_chain.py) | O(n log n) time, O(n) space | [Explanation](notes/longest_interval_chain.md) |
| 208 | [Minimum resources for overlapping half-open intervals](arrays/minimum_parallel_resources.py) | O(n log n) time, O(n) space | [Explanation](notes/minimum_parallel_resources.md) |
| 209 | [Most equal values after bounded independent adjustments](arrays/max_equal_after_adjustments.py) | O(n log n) time, O(n) space | [Explanation](notes/max_equal_after_adjustments.md) |
| 210 | [Minimize the largest difference among disjoint pairs](arrays/minimize_max_pair_difference.py) | O(n log n + n log(D + 1)) time, O(n) space | [Explanation](notes/minimize_max_pair_difference.md) |
| 211 | [Minimize the largest value by transferring units left](arrays/minimize_max_after_left_moves.py) | O(n) time, O(1) space | [Explanation](notes/minimize_max_after_left_moves.md) |
| 212 | [Fastest synchronous neighbor copying on a circular array](arrays/minimum_circular_equalization_seconds.py) | Expected O(n) time, O(n) space | [Explanation](notes/minimum_circular_equalization_seconds.md) |
| 213 | [Fewest adjacent swaps to alternate a binary array](arrays/min_adjacent_swaps_alternating.py) | O(n) time, O(n) space | [Explanation](notes/min_adjacent_swaps_alternating.md) |
| 214 | [Fewest decrements to make alternating strict valleys](arrays/minimum_decrements_zigzag.py) | O(n) time, O(1) space | [Explanation](notes/minimum_decrements_zigzag.md) |
| 215 | [Count strictly increasing or decreasing index triplets](arrays/count_monotone_triplets.py) | O(n squared) time, O(1) auxiliary space | [Explanation](notes/count_monotone_triplets.md) |
| 216 | [Count index quadruplets with a target sum](arrays/count_target_quadruplets.py) | Expected O(n squared) time, O(n squared) space | [Explanation](notes/count_target_quadruplets.md) |
| 217 | [Count target-sum choices from four separate arrays](arrays/four_array_sum_count.py) | Expected O(ab + cd) time, O(ab) space | [Explanation](notes/four_array_sum_count.md) |
| 218 | [Count ordered four-index tuples with equal pair products](arrays/count_equal_product_tuples.py) | Expected O(n squared) time, O(n squared) space | [Explanation](notes/count_equal_product_tuples.md) |
| 219 | [Longest interval with a strict majority above a threshold](arrays/longest_majority_above_threshold.py) | O(n) time, O(n) space | [Explanation](notes/longest_majority_above_threshold.md) |
| 220 | [Partition ordered jobs into days with minimum difficulty](arrays/minimum_job_schedule_difficulty.py) | O(dn squared) time, O(n) space | [Explanation](notes/minimum_job_schedule_difficulty.md) |
| 221 | [Maximum coins from removing balloons in any order](arrays/max_burst_balloon_coins.py) | O(n cubed) time, O(n squared) space | [Explanation](notes/max_burst_balloon_coins.md) |
| 222 | [Minimum triangulation score of a cyclic value array](arrays/minimum_triangulation_score.py) | O(n cubed) time, O(n squared) space | [Explanation](notes/minimum_triangulation_score.md) |
| 223 | [Minimum cost to merge adjacent groups of k piles](arrays/minimum_adjacent_k_merge_cost.py) | O(n cubed) time, O(n squared) space | [Explanation](notes/minimum_adjacent_k_merge_cost.md) |
| 224 | [Partition an array into equal pairs or valid triples](arrays/has_valid_block_partition.py) | O(n) time, O(n) space | [Explanation](notes/has_valid_block_partition.md) |
| 225 | [Maximum subarray sum after squaring exactly one element](arrays/max_subarray_one_square.py) | O(n) time, O(1) space | [Explanation](notes/max_subarray_one_square.md) |
| 226 | [Largest array total after one matching segment exchange](arrays/max_spliced_array_sum.py) | O(n) time, O(1) auxiliary space | [Explanation](notes/max_spliced_array_sum.md) |
| 227 | [Maximum forward path sum across two sorted arrays](arrays/max_two_array_path_sum.py) | O(n + m) time, O(1) auxiliary space | [Explanation](notes/max_two_array_path_sum.md) |
| 228 | [Minimize the range under parity-based value operations](arrays/minimum_array_deviation.py) | O(n log(M + 1) log(n + 1)) time, O(n) space | [Explanation](notes/minimum_array_deviation.md) |
| 229 | [Smallest value range covering every sorted input array](arrays/smallest_covering_range.py) | O(N + N log(k + 1)) time, O(k) space | [Explanation](notes/smallest_covering_range.md) |
| 230 | [Kth smallest element of a row-and-column sorted matrix](arrays/kth_smallest_sorted_matrix.py) | O(rc + k log(r + 1)) time, O(r) space | [Explanation](notes/kth_smallest_sorted_matrix.md) |
| 231 | [Read a rectangular array in clockwise spiral order](arrays/spiral_matrix_values.py) | O(r + rc) time, O(rc) output space | [Explanation](notes/spiral_matrix_values.md) |
| 232 | [Rotate a square array clockwise in place](arrays/rotate_square_clockwise.py) | O(n squared) time, O(1) auxiliary space | [Explanation](notes/rotate_square_clockwise.md) |
| 233 | [Zero every row and column containing an original zero](arrays/zero_matrix_rows_columns.py) | O(r + rc) time, O(1) auxiliary space | [Explanation](notes/zero_matrix_rows_columns.md) |
| 234 | [Largest all-one rectangle in a binary matrix](arrays/max_binary_matrix_rectangle.py) | O(r + rc) time, O(c) auxiliary space | [Explanation](notes/max_binary_matrix_rectangle.md) |
| 235 | [Count all square submatrices filled with ones](arrays/count_all_one_squares.py) | O(r + rc) time, O(c) auxiliary space | [Explanation](notes/count_all_one_squares.md) |
| 236 | [Answer half-open rectangle sums with two-dimensional prefixes](arrays/matrix_rectangle_sums.py) | O(r + rc + q) time, O((r + 1)(c + 1) + q) space | [Explanation](notes/matrix_rectangle_sums.md) |
| 237 | [Count rectangular submatrices with a target sum](arrays/count_target_submatrices.py) | O(r + r squared c) expected time, O(c) auxiliary space | [Explanation](notes/count_target_submatrices.md) |
| 238 | [Maximum sum of a nonempty rectangular submatrix](arrays/max_submatrix_sum.py) | O(r + r squared c) time, O(c) auxiliary space | [Explanation](notes/max_submatrix_sum.md) |
| 239 | [Largest rectangular sum not exceeding a limit](arrays/max_rectangle_sum_bounded.py) | O(r + r squared c squared) time, O(c) auxiliary space | [Explanation](notes/max_rectangle_sum_bounded.md) |
| 240 | [Minimum right-and-down path sum through a matrix](arrays/minimum_grid_path_sum.py) | O(r + rc) time, O(c) auxiliary space | [Explanation](notes/minimum_grid_path_sum.md) |
| 241 | [Count right-and-down paths avoiding blocked cells](arrays/count_grid_paths_obstacles.py) | O(r + rc) time, O(c) auxiliary space | [Explanation](notes/count_grid_paths_obstacles.md) |
| 242 | [Minimum top-to-bottom path with neighboring columns](arrays/minimum_falling_path_sum.py) | O(r + rc) time, O(c) auxiliary space | [Explanation](notes/minimum_falling_path_sum.md) |
| 243 | [Longest strictly increasing path through adjacent cells](arrays/longest_increasing_matrix_path.py) | O(r + rc) time, O(rc) space | [Explanation](notes/longest_increasing_matrix_path.md) |
| 244 | [Traverse matrix diagonals in alternating directions](arrays/diagonal_zigzag_values.py) | O(r + rc) time, O(rc) output space | [Explanation](notes/diagonal_zigzag_values.md) |
| 245 | [Sum the clipped square neighborhood of every matrix cell](arrays/matrix_block_sums.py) | O(r + rc) time, O((r + 1)(c + 1)) space | [Explanation](notes/matrix_block_sums.md) |
| 246 | [Count negatives in a nonincreasing row-and-column matrix](arrays/count_sorted_matrix_negatives.py) | O(r + c) time, O(1) space | [Explanation](notes/count_sorted_matrix_negatives.md) |
| 247 | [Search a row-and-column sorted matrix by its boundary](arrays/contains_sorted_matrix_value.py) | O(r + c) time, O(1) space | [Explanation](notes/contains_sorted_matrix_value.md) |
| 248 | [Reshape a rectangular array while preserving row-major order](arrays/reshape_rectangular_array.py) | O(r + R + rc) time, O(R + rc) output space | [Explanation](notes/reshape_rectangular_array.md) |
| 249 | [Count splits into three nonempty equal-sum array parts](arrays/count_three_equal_sum_partitions.py) | O(n) time, O(1) space | [Explanation](notes/count_three_equal_sum_partitions.md) |
| 250 | [Length of the shortest roll sequence absent as a subsequence](arrays/shortest_missing_roll_sequence.py) | Expected O(n) time, O(min(n, k)) space | [Explanation](notes/shortest_missing_roll_sequence.md) |
| 251 | [Maximum signed subset sum divisible by a chosen modulus](arrays/max_subset_sum_divisible.py) | O(nm) time, O(m) space | [Explanation](notes/max_subset_sum_divisible.md) |
| 252 | [Fewest reusable coin denominations needed for a target](arrays/minimum_coin_count.py) | O(n + d log d + dT + T) time, O(d + T) space | [Explanation](notes/minimum_coin_count.md) |
| 253 | [Count unordered reusable-coin combinations for a target](arrays/count_coin_combinations.py) | O(n + d log d + dT + T) time, O(d + T) space | [Explanation](notes/count_coin_combinations.md) |
| 254 | [Count ordered sequences of reusable array values with a target sum](arrays/count_ordered_target_sums.py) | O(n + d log d + dT + T) time, O(d + T) space | [Explanation](notes/count_ordered_target_sums.md) |
| 255 | [Longest subsequence where each value sums the preceding two](arrays/longest_fibonacci_subsequence.py) | Expected O(n squared) time, O(n squared) space | [Explanation](notes/longest_fibonacci_subsequence.md) |
| 256 | [Longest reorderable chain of repeated squaring](arrays/longest_square_streak.py) | O(n + u log u) arithmetic operations, O(u) space | [Explanation](notes/longest_square_streak.md) |
| 257 | [Maximum nesting chain of width-height pairs](arrays/maximum_envelope_nesting.py) | O(n log(n + 1)) time, O(n) space | [Explanation](notes/maximum_envelope_nesting.md) |
| 258 | [Reconstruct indices of a longest increasing subsequence](arrays/reconstruct_lis_indices.py) | O(n log(n + 1)) time, O(n) space | [Explanation](notes/reconstruct_lis_indices.md) |
| 259 | [Longest strictly increasing subsequence common to two arrays](arrays/longest_common_increasing_subsequence.py) | O(nm) time, O(m) space | [Explanation](notes/longest_common_increasing_subsequence.md) |
| 260 | [Delete the fewest values until the minimum divides another array](arrays/minimum_deletions_for_divisor.py) | O(n log n + m) GCD/arithmetic operations, O(n) space | [Explanation](notes/minimum_deletions_for_divisor.md) |
| 261 | [Fewest neighbor-GCD replacements to make every value one](arrays/minimum_neighbor_gcd_operations.py) | O(n squared) GCD operations, O(1) auxiliary space | [Explanation](notes/minimum_neighbor_gcd_operations.md) |
| 262 | [Maximize round-weighted GCD scores over disjoint pairs](arrays/max_weighted_gcd_pairing.py) | O(n squared 2^n) time, O(2^n + n squared) space | [Explanation](notes/max_weighted_gcd_pairing.md) |
| 263 | [Count distinct nonempty value subsequences](arrays/count_distinct_value_subsequences.py) | Expected O(n) arithmetic operations, O(n) auxiliary slots | [Explanation](notes/count_distinct_value_subsequences.md) |
| 264 | [Select a ranked permutation of distinct array values](arrays/kth_lexicographic_permutation.py) | O(n squared) arithmetic/list operations, O(n) auxiliary slots | [Explanation](notes/kth_lexicographic_permutation.md) |
| 265 | [Rank an array among its distinct multiset permutations](arrays/multiset_permutation_rank.py) | O(nu + n + u log u) arithmetic operations, O(u) auxiliary slots | [Explanation](notes/multiset_permutation_rank.md) |
| 266 | [Pair two arrays to minimize total absolute difference](arrays/minimum_absolute_pairing_cost.py) | O(n log n) time, O(n) space | [Explanation](notes/minimum_absolute_pairing_cost.md) |
| 267 | [Reorder values to maximize the total of requested ranges](arrays/maximize_requested_range_sum.py) | O(n log n + q) time, O(n) space | [Explanation](notes/maximize_requested_range_sum.md) |
| 268 | [Fewest same-index swaps making both arrays strictly increasing](arrays/minimum_swaps_increasing_arrays.py) | O(n) time, O(1) auxiliary space | [Explanation](notes/minimum_swaps_increasing_arrays.md) |
| 269 | [Minimum radius-array taps covering a continuous garden](arrays/minimum_garden_taps.py) | O(n) time, O(n) space | [Explanation](notes/minimum_garden_taps.md) |
| 270 | [Minimum cost of one-day, seven-day and thirty-day travel passes](arrays/minimum_travel_ticket_cost.py) | O(n log(n + 1)) time, O(n) space | [Explanation](notes/minimum_travel_ticket_cost.md) |
| 271 | [Assign reusable jobs to workers for maximum total profit](arrays/max_worker_assignment_profit.py) | O(n log n + m log m) time, O(n + m) space | [Explanation](notes/max_worker_assignment_profit.md) |
| 272 | [Count subarrays whose lower median is a given distinct value](arrays/count_subarrays_median_value.py) | Expected O(n) time, O(n) space | [Explanation](notes/count_subarrays_median_value.md) |
| 273 | [Count windows whose sum times length is below a limit](arrays/count_subarrays_below_score.py) | O(n) time, O(1) space | [Explanation](notes/count_subarrays_below_score.md) |
| 274 | [Fewest deletions leaving an even array of unequal neighbor pairs](arrays/minimum_deletions_unequal_pairs.py) | O(n) time, O(1) space | [Explanation](notes/minimum_deletions_unequal_pairs.md) |
| 275 | [Empty an array by removing equal-value pairs or triples](arrays/minimum_equal_group_removals.py) | Expected O(n) time, O(n) space | [Explanation](notes/minimum_equal_group_removals.md) |
| 276 | [Maximum increasing-size groups under per-value usage limits](arrays/maximum_increasing_usage_groups.py) | O(n log n) time, O(n) space | [Explanation](notes/maximum_increasing_usage_groups.md) |
| 277 | [Minimum cross-array swap cost to equalize two multisets](arrays/minimum_basket_swap_cost.py) | O(n log n) time, O(n) space | [Explanation](notes/minimum_basket_swap_cost.md) |
| 278 | [Build a nonnegative target using unit subarray increments](arrays/minimum_range_increments.py) | O(n) time, O(1) space | [Explanation](notes/minimum_range_increments.md) |
| 279 | [Transform one array into another with unit interval additions](arrays/minimum_signed_range_operations.py) | O(n) time, O(1) auxiliary space | [Explanation](notes/minimum_signed_range_operations.md) |
| 280 | [Count strict 1324-pattern index quadruplets](arrays/count_1324_quadruplets.py) | O(n squared) time, O(n) space | [Explanation](notes/count_1324_quadruplets.md) |
| 281 | [Split an array into two nonempty groups with equal averages](arrays/can_split_same_average.py) | Expected O(n squared R) time, O(nR) space | [Explanation](notes/can_split_same_average.md) |
| 282 | [Smallest distance from a target to any subset sum](arrays/closest_subset_sum_difference.py) | O(n 2^ceil(n/2)) time, O(2^ceil(n/2)) space | [Explanation](notes/closest_subset_sum_difference.md) |
| 283 | [Partition into equal-sized groups with minimum sum difference](arrays/minimum_balanced_partition_difference.py) | O(n 2^(n/2)) time, O(2^(n/2)) space | [Explanation](notes/minimum_balanced_partition_difference.md) |
| 284 | [Count contiguous partitions that never split equal values](arrays/count_value_disjoint_partitions.py) | Expected O(n) arithmetic operations, O(n) space | [Explanation](notes/count_value_disjoint_partitions.md) |
| 285 | [Count nonempty index subsets avoiding a fixed value difference](arrays/count_subsets_avoiding_difference.py) | O(n + u log u) arithmetic operations, O(u) auxiliary slots | [Explanation](notes/count_subsets_avoiding_difference.md) |
