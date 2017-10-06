# Playing 2048 game with an Automated Bot.

Bot uses Expectimax search with the depth of 4 to find the best possible move.

Project is still in progress. During testing 1024 tile was produced every time and 2048 tile in 60% of the games.

# Prerequisites

Game theory, Machine Learning, Minmax, Expectimax

# Files Info

direct.py --> Expectimax implementation (main algorithm)

puzzle.py ---> Implementation of game (main file, run this file for demo)

logic.py ----> Implementation of game (backend)

merge_game.py -----> Helper file for merging the matrix

## Demo

```$ git clone https://github.com/vpn1997/2048-Ai```

```$ cd 2048-Ai```

```$ pip install requirements.txt```

```$ python puzzle.py```

![webp net-resizeimage 2](https://user-images.githubusercontent.com/17298412/31058099-8a9077a4-a70b-11e7-99bb-e55cd540bb6d.png)

## Heuristics

(In file direct.py)

I have used a score and a penalty function.

A configuration gets a high score if it follows snake line pattern.

Weights are assigned to individual tiles. You can tweak them to get better results.

Penalty is given depending on how many filled tiles are present (more filled tiles => bigger penalty).

You can download the game interface from https://github.com/yangshun/2048-python.

## Future work

1. Getting 2048 or bigger tiles at higher frequency.

2. Using Reinforcement learning didn't give any promising results.

The highest tile it used to get during the game was 128.
  
So still working on improving that model.

## Reference
https://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048
