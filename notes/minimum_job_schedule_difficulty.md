# Partition ordered jobs into days with minimum difficulty

A day handles a nonempty contiguous block and costs its maximum difficulty. For each number of days and prefix endpoint, extend the final block backward while maintaining its maximum. Combine it with the optimum schedule of the preceding prefix.

Complexity: O(dn squared) time, O(n) space.

- [Implementation](../arrays/minimum_job_schedule_difficulty.py)
- [Tests](../tests/test_minimum_job_schedule_difficulty.py)

Run this exercise: `python -m unittest tests.test_minimum_job_schedule_difficulty -v`
