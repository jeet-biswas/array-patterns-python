# Count subarrays with a specified greatest common divisor

Compress suffixes ending at each position by their GCD, retaining a count per result. Extending a suffix replaces its GCD by the GCD with the new value. Distinct positive GCDs form a divisor chain of logarithmic length; M is the maximum value. Euclidean GCD operation costs are additional.

Complexity: O(n log(M + 1)) GCD operations, O(log(M + 1)) states.

- [Implementation](../arrays/count_subarray_gcd.py)
- [Tests](../tests/test_count_subarray_gcd.py)

Run this exercise: `python -m unittest tests.test_count_subarray_gcd -v`
