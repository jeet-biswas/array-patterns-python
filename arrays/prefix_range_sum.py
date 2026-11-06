class PrefixRangeSum:
    """Snapshot array sums. Build: O(n) time/space; query: O(1).

    sum_range uses [start, stop), allowing empty ranges. Out-of-bounds or
    reversed ranges raise IndexError; negative indexing is not supported.
    """
    def __init__(self, values: list[int]):
        self._prefix = [0]
        for value in values:
            self._prefix.append(self._prefix[-1] + value)

    def sum_range(self, start: int, stop: int) -> int:
        if not 0 <= start <= stop < len(self._prefix):
            raise IndexError('expected 0 <= start <= stop <= array length')
        return self._prefix[stop] - self._prefix[start]
