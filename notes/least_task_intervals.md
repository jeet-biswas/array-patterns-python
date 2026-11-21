# Minimum scheduling slots for repeated tasks with cooldown

The most frequent labels form a frame separated by cooldown slots. If f is their frequency and c labels share it, that frame needs (f-1)*(cooldown+1)+c slots. Other tasks fill the gaps, so the result is the maximum of this bound and the task count. u is the number of task labels.

Complexity: Expected O(n) time, O(u) space.

- [Implementation](../arrays/least_task_intervals.py)
- [Tests](../tests/test_least_task_intervals.py)

Run this exercise: `python -m unittest tests.test_least_task_intervals -v`
