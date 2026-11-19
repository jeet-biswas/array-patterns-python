class WeightedRangeSum:
    """Snapshot an integer array for relative-weight range queries.

    O(n) construction and space; O(1) arithmetic operations per query.
    """
    def __init__(self, values: list[int]):
        self._plain = [0]
        self._weighted = [0]
        for i, value in enumerate(values, 1):
            self._plain.append(self._plain[-1] + value)
            self._weighted.append(self._weighted[-1] + i * value)

    def query(self, start: int, stop: int) -> int:
        """Sum values[start+j]*(j+1) over [start, stop); empty -> 0.

        Invalid/reversed bounds raise IndexError.
        """
        if not 0 <= start <= stop < len(self._plain):
            raise IndexError('expected 0 <= start <= stop <= length')
        plain = self._plain[stop] - self._plain[start]
        return self._weighted[stop] - self._weighted[start] - start * plain
