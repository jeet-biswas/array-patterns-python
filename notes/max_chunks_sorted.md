# Maximum independently sortable chunks

Store each candidate chunk's maximum on a stack. When a value falls below a previous maximum, merge all incompatible chunks while retaining their largest maximum. Equal boundary values may stay in separate chunks.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/max_chunks_sorted.py)
- [Tests](../tests/test_max_chunks_sorted.py)

Run this exercise: `python -m unittest tests.test_max_chunks_sorted -v`
