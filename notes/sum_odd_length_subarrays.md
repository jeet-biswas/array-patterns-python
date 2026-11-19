# Sum of all odd-length subarrays

Count how many odd-length subarrays contain each element. Of (i+1)*(n-i) possible left/right endpoint combinations, the ceiling of half have odd length. Multiply that count by the element instead of enumerating subarrays.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/sum_odd_length_subarrays.py)
- [Tests](../tests/test_sum_odd_length_subarrays.py)

Run this exercise: `python -m unittest tests.test_sum_odd_length_subarrays -v`
