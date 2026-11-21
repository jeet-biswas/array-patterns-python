def visible_people_right(heights: list[int]) -> list[int]:
    """Count j>i where all intermediate heights are below min(heights[i], heights[j]).

    Heights must be distinct positive integers; input is unchanged.
    """
    if any(x <= 0 for x in heights) or len(set(heights)) != len(heights):
        raise ValueError('distinct positive heights required')
    result = [0] * len(heights)
    stack = []
    for i in range(len(heights)-1, -1, -1):
        while stack and stack[-1] < heights[i]:
            stack.pop()
            result[i] += 1
        if stack:
            result[i] += 1
        stack.append(heights[i])
    return result
