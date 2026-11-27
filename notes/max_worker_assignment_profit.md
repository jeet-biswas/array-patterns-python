# Assign reusable jobs to workers for maximum total profit

Sort jobs by difficulty and workers by ability. Advance through newly feasible jobs while retaining the best available profit. Every worker can independently take that best job because jobs are reusable; a worker may also remain unassigned.

Complexity: O(n log n + m log m) time, O(n + m) space.

- [Implementation](../arrays/max_worker_assignment_profit.py)
- [Tests](../tests/test_max_worker_assignment_profit.py)

Run this exercise: `python -m unittest tests.test_max_worker_assignment_profit -v`
