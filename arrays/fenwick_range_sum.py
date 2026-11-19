class FenwickRangeSum:
    """Integer array sums with point increments; input copied, not shared.

    O(n) build/space; O(log(n+1)) add/query operations.
    """
    def __init__(self, values: list[int]):
        self._length = len(values)
        self._tree = [0] + values.copy()
        for i in range(1, self._length + 1):
            parent = i + (i & -i)
            if parent <= self._length:
                self._tree[parent] += self._tree[i]

    def add(self, index: int, delta: int) -> None:
        """Increment one zero-based element; invalid index raises IndexError."""
        if not 0 <= index < self._length:
            raise IndexError('index is outside the array')
        i = index + 1
        while i <= self._length:
            self._tree[i] += delta
            i += i & -i

    def _prefix(self, stop):
        total = 0
        while stop:
            total += self._tree[stop]
            stop -= stop & -stop
        return total

    def query(self, start: int, stop: int) -> int:
        """Sum of [start, stop); invalid/reversed bounds raise IndexError."""
        if not 0 <= start <= stop <= self._length:
            raise IndexError('expected 0 <= start <= stop <= length')
        return self._prefix(stop) - self._prefix(start)
