import math
from merge_game import *
from logic import *
import itertools
import numpy as np


def direction(matrix):
    def search(matrix, depth, move=False):
        # if on leave node return the score or if the game is over
        l = game_state(matrix)

        if (l == 'win' or l == 'lose'):
            l = 1
        else:
            l = 0

        if depth == 0 or (move and l):
            return heuristic(matrix)

        alpha = heuristic(matrix)

        if move:
            for _, action in MERGE_FUNCTIONS.items():
                child = action(matrix)
                alpha = max(alpha, search(child, depth - 1))


        else:
            alpha = 0
            zeros = [(i, j) for i, j in itertools.product(range(4), range(4)) if matrix[i][j] == 0]
            for i, j in zeros:
                c1 = [[x for x in row] for row in matrix]
                c2 = [[x for x in row] for row in matrix]
                c1[i][j] = 2
                c2[i][j] = 4
                alpha += (.9 * search(c1, depth - 1, True) / len(zeros) +
                          .1 * search(c2, depth - 1, True) / len(zeros))
        return alpha

    def heuristic(matrix):

        snake = []
        for i, col in enumerate(zip(*matrix)):
            snake.extend(reversed(col) if i % 2 == 0 else col)

        m = max(snake)
        return sum(x / 10 ** n for n, x in enumerate(snake)) - \
               math.pow((matrix[3][0] != m) * abs(matrix[3][0] - m), 2)

    results = []
    for direction, action in MERGE_FUNCTIONS.items():
        if matrix != action(matrix):
            result = direction, search(action(matrix), 4)

            results.append(result)
    print results
    return max(results, key=lambda x: x[1])[0]

