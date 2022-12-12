"""Day 9: Rope Bridge"""
# pylint: disable=invalid-name
import math


DIRECTIONS = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}


class Knot:
    """Knot with a position and history of visited positons."""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = {(0,0)}

    def move(self, x, y):
        """Move the knot by (x,y) and mark this position as visited."""
        self.x += x
        self.y += y
        self.visited.add((self.x, self.y))


def update_adjacent(a, b):
    """Update the positons of knot `b` to follow adjacent knot `a`."""
    dx, dy = a.x - b.x, a.y - b.y
    while max(abs(dx), abs(dy)) > 1:
        b.move(
            int(math.copysign(min(max(abs(dx), 0), 1), dx)),
            int(math.copysign(min(max(abs(dy), 0), 1), dy))
        )
        dx, dy = a.x - b.x, a.y - b.y


def simulate_rope(n_knots, moves):
    """Simulate movement of a rope with n_knots."""
    knots = [Knot() for _ in range(n_knots)]
    for move in moves:
        (direction, steps) = move
        for _ in range(steps):
            knots[0].move(*DIRECTIONS[direction])
            for i in range(len(knots)-1):
                update_adjacent(knots[i], knots[i+1])

    return knots


if __name__ == '__main__':
    with open('input09.txt', 'r', encoding='utf-8') as input_file:
        moves_raw = input_file.read().splitlines()

    input_moves = [
        (direction, int(steps))
        for (direction, steps) in [move.split(' ') for move in moves_raw]
    ]

    print(len(simulate_rope(2, input_moves)[-1].visited))
    print(len(simulate_rope(10, input_moves)[-1].visited))
