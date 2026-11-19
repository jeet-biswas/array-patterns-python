class RangeMinTable:
    """Immutable range minima; O(n log(n+1)) build/space, O(1) query operations."""
    def __init__(self, values: list[int]):
        self._length = len(values)
        self._table = [values.copy()]
        span = 2
        while span <= len(values):
            previous = self._table[-1]
            half = span // 2
            self._table.append([min(previous[i], previous[i+half])
                                for i in range(len(values)-span+1)])
            span *= 2

    def query(self, start: int, stop: int) -> int:
        """Minimum of nonempty [start, stop); invalid bounds raise IndexError."""
        if not 0 <= start < stop <= self._length:
            raise IndexError('expected 0 <= start < stop <= length')
        level = (stop - start).bit_length() - 1
        span = 1 << level
        return min(self._table[level][start], self._table[level][stop-span])
