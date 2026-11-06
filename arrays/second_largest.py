def second_largest(values: list[int]) -> int | None:
    """Return the second largest distinct integer, or None if it does not exist.

    O(n) time and O(1) extra space. Does not sort or modify the input.
    """
    largest = runner_up = None
    for value in values:
        if largest is None or value > largest:
            runner_up, largest = largest, value
        elif value != largest and (runner_up is None or value > runner_up):
            runner_up = value
    return runner_up
