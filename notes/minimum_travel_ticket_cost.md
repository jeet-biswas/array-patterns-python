# Minimum cost of one-day, seven-day and thirty-day travel passes

For each first uncovered travel day, buying a pass covers a consecutive prefix of remaining travel days. Binary-search the first uncovered day for each duration and combine its optimal suffix cost. Travel days need not be consecutive calendar days.

Complexity: O(n log(n + 1)) time, O(n) space.

- [Implementation](../arrays/minimum_travel_ticket_cost.py)
- [Tests](../tests/test_minimum_travel_ticket_cost.py)

Run this exercise: `python -m unittest tests.test_minimum_travel_ticket_cost -v`
