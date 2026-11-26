# Longest strictly increasing path through adjacent cells

Direct edges from smaller cells to larger neighbors. Count each cell's smaller predecessors, then remove zero-indegree cells layer by layer. Strict increase makes this graph acyclic, and the number of topological layers equals the longest path length without recursive stack limits.

Complexity: O(r + rc) time, O(rc) space.

- [Implementation](../arrays/longest_increasing_matrix_path.py)
- [Tests](../tests/test_longest_increasing_matrix_path.py)

Run this exercise: `python -m unittest tests.test_longest_increasing_matrix_path -v`
