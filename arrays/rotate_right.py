def rotate_right(values: list[int], steps: int) -> None:
    """Rotate in place; negative steps rotate left. Empty input is unchanged.

    O(n) time, O(1) extra space; returns None.
    """
    if not values:
        return
    steps %= len(values)
    if steps == 0:
        return

    def reverse(left, right):
        while left < right:
            values[left], values[right] = values[right], values[left]
            left += 1
            right -= 1

    reverse(0, len(values) - 1)
    reverse(0, steps - 1)
    reverse(steps, len(values) - 1)
