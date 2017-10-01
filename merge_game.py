def merge_right(b):

    def reverse(x):
        return list(reversed(x))

    t = map(reverse, b)
    return [reverse(x) for x in merge_left(t)]


def merge_up(b):

    t = merge_left(zip(*b))
    return [list(x) for x in zip(*t)]


def merge_down(b):

    t = merge_right(zip(*b))
    return [list(x) for x in zip(*t)]


def merge_left(b):


    def merge(row, acc):


        if not row:
            return acc

        x = row[0]
        if len(row) == 1:
            return acc + [x]

        return merge(row[2:], acc + [2 * x]) if x == row[1] else merge(row[1:], acc + [x])

    board = []
    for row in b:
        merged = merge([x for x in row if x != 0], [])
        merged = merged + [0] * (len(row) - len(merged))
        board.append(merged)
    return board


def move_exists(b):

    for row in b:
        for x, y in zip(row[:-1], row[1:]):
            if x == y or x == 0 or y == 0:
                return True
    return False


MERGE_FUNCTIONS = {
    'left': merge_left,
    'right': merge_right,
    'up': merge_up,
    'down': merge_down
}
