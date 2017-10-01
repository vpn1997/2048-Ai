# Playing 2048 game with an automated bot.
Bot uses Expectimax search with depth of 4 to find the best possible move.
Project is still in progress.It can play upto 1024(90%) and only once i got 
2048 tile , so its still not good enough.
## Heuristics
I hace used score and penalty function.
A configuration Gets a high score if it follows snake line pattern.
Weights are assigned to individual tiles.U can tweek them to get better results.
Penalty is given if u have too many empty tiles.
U can download the game interface from https://github.com/yangshun/2048-python.

### Future work
1.Getting 2048  tiles or more at higher freq.
2.Using Reinforcement learing(one i am using gives tiles upto only 128 :p)


