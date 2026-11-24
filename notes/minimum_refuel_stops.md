# Fewest fuel stops needed to reach a destination

Treat current fuel reach as a frontier. Add all reachable station fuel amounts to a max-heap, and whenever progress needs another stop take the largest available amount. This retroactive choice maximizes reach after each number of stops without changing which past stations were reachable.

Complexity: O(n log(n + 1)) time, O(n) space.

- [Implementation](../arrays/minimum_refuel_stops.py)
- [Tests](../tests/test_minimum_refuel_stops.py)

Run this exercise: `python -m unittest tests.test_minimum_refuel_stops -v`
