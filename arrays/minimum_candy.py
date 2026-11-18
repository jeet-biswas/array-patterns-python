def minimum_candy(ratings: list[int]) -> int:
    """Minimum positive candies with more candies than any lower-rated neighbor.

    Equal ratings impose no ordering. Empty -> 0; signed ratings allowed.
    O(n) time, O(n) space; input is unchanged.
    """
    candies = [1] * len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)
