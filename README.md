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
