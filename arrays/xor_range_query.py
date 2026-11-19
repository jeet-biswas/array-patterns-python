class XorRangeQuery:
    """Snapshot integer array XORs; O(n) construction/space, O(1) query ops.

    Bit-operation costs depend on integer sizes; signed integers supported.
    """
    def __init__(self, values: list[int]):
        self._prefix = [0]
        for value in values:
            self._prefix.append(self._prefix[-1] ^ value)

    def query(self, start: int, stop: int) -> int:
        """XOR of [start, stop); invalid/reversed bounds raise IndexError."""
        if not 0 <= start <= stop < len(self._prefix):
            raise IndexError('expected 0 <= start <= stop <= length')
        return self._prefix[stop] ^ self._prefix[start]
