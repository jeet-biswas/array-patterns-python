def count_smaller_right(values: list[int]) -> list[int]:
    """At each position, count strictly smaller elements to its right.

    O(n log(n+1)) time and O(n) space, including output. No mutation.
    """
    ranks = {value: i + 1 for i, value in enumerate(sorted(set(values)))}
    tree = [0] * (len(ranks) + 1)
    result = [0] * len(values)
    for i in range(len(values) - 1, -1, -1):
        rank = ranks[values[i]]
        position = rank - 1
        while position:
            result[i] += tree[position]
            position -= position & -position
        position = rank
        while position < len(tree):
            tree[position] += 1
            position += position & -position
    return result
