# Compute consecutive backward stock spans

A span ends just after the nearest earlier strictly greater reading. Maintain those candidate indices on a decreasing stack, removing smaller-or-equal readings as they become dominated.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/stock_spans.py)
- [Tests](../tests/test_stock_spans.py)

Run this exercise: `python -m unittest tests.test_stock_spans -v`
