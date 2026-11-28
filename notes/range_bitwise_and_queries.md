# Answer static range AND queries with a sparse table

Build AND summaries for every power-of-two block size. A query combines two blocks of the largest fitting size, one at each endpoint. Overlap is safe because applying AND to the same value twice has no further effect. Bounded integer bit costs are additional.

Complexity: O(n log(n + 1) + q) bitwise operations, O(n log(n + 1) + q) space.

- [Implementation](../arrays/range_bitwise_and_queries.py)
- [Tests](../tests/test_range_bitwise_and_queries.py)

Run this exercise: `python -m unittest tests.test_range_bitwise_and_queries -v`
