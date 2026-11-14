def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Days to the next strictly warmer reading; zero means no later warmer day.

    Any integer temperatures are allowed. O(n) time and O(n) space.
    Input is not modified.
    """
    result = [0] * len(temperatures)
    waiting = []
    for day, temperature in enumerate(temperatures):
        while waiting and temperatures[waiting[-1]] < temperature:
            previous = waiting.pop()
            result[previous] = day - previous
        waiting.append(day)
    return result
