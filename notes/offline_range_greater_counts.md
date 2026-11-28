# Count values above query thresholds inside array ranges

Process queries by decreasing threshold and activate array positions whose values are strictly greater. A Fenwick tree stores one at each active position, making each range count a difference of two prefix counts. Answers are restored to input query order.

Complexity: O((n + q) log(n + q + 2)) time, O(n + q) space.

- [Implementation](../arrays/offline_range_greater_counts.py)
- [Tests](../tests/test_offline_range_greater_counts.py)

Run this exercise: `python -m unittest tests.test_offline_range_greater_counts -v`
