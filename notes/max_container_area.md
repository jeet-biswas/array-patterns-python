# Container with most water

Start with the widest container. Move the shorter boundary inward because retaining it cannot improve the area when width decreases. This differs from summing water trapped between bars.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/max_container_area.py)
- [Tests](../tests/test_max_container_area.py)

Run this exercise: `python -m unittest tests.test_max_container_area -v`
