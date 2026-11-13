# Count inversions using merge sort

During a sorted merge, a right element smaller than the current left element forms an inversion with every unconsumed element of the left half. Count these in bulk, preserving the caller's input by working on a copy.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/inversion_count.py)
- [Tests](../tests/test_inversion_count.py)

Run this exercise: `python -m unittest tests.test_inversion_count -v`
