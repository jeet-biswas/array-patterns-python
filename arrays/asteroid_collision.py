def asteroid_collision(asteroids: list[int]) -> list[int]:
    """Survivors for equal-speed asteroids: sign is direction, magnitude is size.

    Equal colliding sizes both disappear; zero raises ValueError.
    O(n) time, O(n) space; input is unchanged.
    """
    if any(value == 0 for value in asteroids):
        raise ValueError('asteroid sizes must be nonzero')
    survivors = []
    for value in asteroids:
        alive = True
        while alive and value < 0 and survivors and survivors[-1] > 0:
            if survivors[-1] < -value:
                survivors.pop()
            elif survivors[-1] == -value:
                survivors.pop()
                alive = False
            else:
                alive = False
        if alive:
            survivors.append(value)
    return survivors
