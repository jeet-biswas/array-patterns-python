# Furthest array position reachable with bricks and ladders

Assign ladders to the largest climbs encountered. A min-heap holds these provisional ladder climbs; when there are too many, pay bricks for the smallest. If that payment exceeds the budget, no assignment can reach the next building. L is the ladder count.

Complexity: O(n log(min(n, L) + 2)) time, O(min(n, L) + 1) space.

- [Implementation](../arrays/furthest_reachable_building.py)
- [Tests](../tests/test_furthest_reachable_building.py)

Run this exercise: `python -m unittest tests.test_furthest_reachable_building -v`
