# Length of the shortest roll sequence absent as a subsequence

Greedily cut the roll array into the maximum number of blocks that each contain every face. Each complete block guarantees one more arbitrary subsequence symbol. A sequence one longer can be chosen to miss the next block boundary, giving the shortest absent length.

Complexity: Expected O(n) time, O(min(n, k)) space.

- [Implementation](../arrays/shortest_missing_roll_sequence.py)
- [Tests](../tests/test_shortest_missing_roll_sequence.py)

Run this exercise: `python -m unittest tests.test_shortest_missing_roll_sequence -v`
