from bisect import bisect_left, insort


def sliding_window_medians(values: list[int], size: int) -> list[float]:
    """Float medians of full windows; require 1 <= size <= n, else ValueError.

    Inputs should have float-representable magnitudes. O(n*size + size*log(size))
    time, O(size) auxiliary space plus output. Input is unchanged.
    """
    if not 1 <= size <= len(values):
        raise ValueError('size must be between one and array length')
    window = sorted(values[:size])
    result = []
    for stop in range(size, len(values) + 1):
        middle = size // 2
        result.append(float(window[middle]) if size % 2 else (window[middle-1]+window[middle])/2)
        if stop < len(values):
            window.pop(bisect_left(window, values[stop-size]))
            insort(window, values[stop])
    return result
