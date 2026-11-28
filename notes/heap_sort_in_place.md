# Sort an array in place using a binary max heap

Build a max heap bottom-up, then repeatedly exchange its maximum with the last active position. Restore the heap by sifting the replacement downward. The sorted suffix grows without recursion or an auxiliary array; equal values need not retain their original order.

Complexity: O(n log(n + 1)) time, O(1) auxiliary space.

- [Implementation](../arrays/heap_sort_in_place.py)
- [Tests](../tests/test_heap_sort_in_place.py)

Run this exercise: `python -m unittest tests.test_heap_sort_in_place -v`
