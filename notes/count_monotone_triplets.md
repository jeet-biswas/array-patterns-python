# Count strictly increasing or decreasing index triplets

Treat each index as the middle of a triplet. Count smaller and larger elements on either side; multiply the compatible counts for increasing and decreasing orders. Equal values never enter a strict triplet.

Complexity: O(n squared) time, O(1) auxiliary space.

- [Implementation](../arrays/count_monotone_triplets.py)
- [Tests](../tests/test_count_monotone_triplets.py)

Run this exercise: `python -m unittest tests.test_count_monotone_triplets -v`
