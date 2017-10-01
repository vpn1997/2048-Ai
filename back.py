import math
from merge_game import *
from logic import *
import itertools
import numpy as np
def direction(matrix):

    def search(matrix,depth,move=False):
        # if on leave node return the score or if the game is over
        l=game_state(matrix)

        if(l=='win' or l=='lose'):
            l=1
        else:
            l=0

        if depth==0  or (move and l ):
            return heuristic(matrix)

        alpha=heuristic(matrix)

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
        def score(matrix):
            weight=[[6,5,4,3],[5,4,3,2],[4,3,2,1],[3,2,1,0]]
            sco=0
            for i in range(0,4):
                for j in range(0,4):

                    sco=sco+int(weight[i][j])*int(matrix[i][j])
            return sco


        def penalty(matrix):

            pen=0
            li=[-1,1]
            for i in range(0,4):
                for j in range(0,4):
                    if(i-1>=0):
                        pen+=abs(matrix[i][j]-matrix[i-1][j])
                    if(i+1<4):
                        pen+=abs(matrix[i][j]-matrix[i+1][j])
                    if (j - 1 >= 0):
                        pen += abs(matrix[i][j] - matrix[i][j-1])
                    if (j + 1 < 4):
                        pen += abs(matrix[i][j] - matrix[i][j+1])

            pen2=0  #for not empty tiles
            for i in range(0,4):
                for j in range(0,4):
                    if(matrix[i][j]):
                        pen2=pen2+1

            return pen-pen2


        return score(matrix)-penalty(matrix)

    results = []
    for direction, action in MERGE_FUNCTIONS.items():
        if matrix!=action(matrix):
            result = direction, search(action(matrix), 4)

            results.append(result)
    print results
    return max(results, key = lambda x: x[1])[0]

import math
from merge_game import *
from logic import *
import itertools
import numpy as np
def direction(matrix):

    def search(matrix,depth,move=False):
        # if on leave node return the score or if the game is over
        l=game_state(matrix)

        if(l=='win' or l=='lose'):
            l=1
        else:
            l=0

        if depth==0  or (move and l ):
            return heuristic(matrix)

        alpha=heuristic(matrix)

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
        def score(matrix):
            weight=[[6,5,4,3],[5,4,3,2],[4,3,2,1],[3,2,1,0]]
            sco=0
            for i in range(0,4):
                for j in range(0,4):

                    sco=sco+int(weight[i][j])*int(matrix[i][j])
            return sco


        def penalty(matrix):

            pen=0
            li=[-1,1]
            for i in range(0,4):
                for j in range(0,4):
                    if(i-1>=0):
                        pen+=abs(matrix[i][j]-matrix[i-1][j])
                    if(i+1<4):
                        pen+=abs(matrix[i][j]-matrix[i+1][j])
                    if (j - 1 >= 0):
                        pen += abs(matrix[i][j] - matrix[i][j-1])
                    if (j + 1 < 4):
                        pen += abs(matrix[i][j] - matrix[i][j+1])

            pen2=0  #for not empty tiles
            for i in range(0,4):
                for j in range(0,4):
                    if(matrix[i][j]):
                        pen2=pen2+1

            return pen-pen2


        return score(matrix)-penalty(matrix)

    results = []
    for direction, action in MERGE_FUNCTIONS.items():
        if matrix!=action(matrix):
            result = direction, search(action(matrix), 4)

            results.append(result)
    print results
    return max(results, key = lambda x: x[1])[0]

