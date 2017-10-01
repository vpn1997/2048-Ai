import math


def aimove(b):

    def fitness(b):


        if not move_exists(b):
            return -float("inf")

        snake = []
        for i, col in enumerate(zip(*b)):
            snake.extend(reversed(col) if i % 2 == 0 else col)

        m = max(snake)
        return sum(x / 10 ** n for n, x in enumerate(snake)) - \
               math.pow((b[3][0] != m) * abs(b[3][0] - m), 2)

    def search(b, d):


        if d == 0 or (not move_exists(b)):
            return fitness(b)

        alpha = fitness(b)

        for _, action in MERGE_FUNCTIONS.items():
            child = action(b)
            alpha = max(alpha, search(child, d - 1))

        return alpha

    results = []
    for direction, action in MERGE_FUNCTIONS.items():
        result = direction, search(action(b), 4)
        results.append(result)
    return results

def give_dir(matrix):
    direction = max(aimove(matrix), key=lambda x: x[1])[0]
    return direction