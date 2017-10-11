try:
    from Tkinter import *
    import Tkinter as tk
except :
    from tkinter import *
    import tkinter as tk
    pass
from logic import *
from random import *
import math
from direct import *
import pyautogui as keybord


SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10
BTN_WIDTH = 12

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {   2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                            32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                            512:"#edc850", 1024:"#edc53f", 2048:"#edc22e" }
CELL_COLOR_DICT = { 2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                    32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                    512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2" }
FONT = ("Verdana", 30, "bold")

KEY_UP_ALT = "\'\\uf700\'"
KEY_DOWN_ALT = "\'\\uf701\'"
KEY_LEFT_ALT = "\'\\uf702\'"
KEY_RIGHT_ALT = "\'\\uf703\'"

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"

class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)
#        self.grid_propagate(0)
        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)

        #self.gamelogic = gamelogic
        self.commands = {   KEY_UP: up, KEY_DOWN: down, KEY_LEFT: left, KEY_RIGHT: right,
                            KEY_UP_ALT: up, KEY_DOWN_ALT: down, KEY_LEFT_ALT: left, KEY_RIGHT_ALT: right }

        self.grid_cells = []
        self.totalScore=0
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells(self.totalScore)
        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=BACKGROUND_COLOR_GAME,
                width=SIZE + GRID_LEN * 2 * GRID_PADDING,
                height=SIZE * (GRID_LEN + 1) / GRID_LEN \
                        + (GRID_LEN + 1) * 2 * GRID_PADDING + BTN_WIDTH
            )
        background.grid_propagate(0)
        background.grid()

        for i in range(GRID_LEN):
            grid_row = []
            for j in range(GRID_LEN):
                cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE/GRID_LEN, height=SIZE/GRID_LEN)
                cell.grid_columnconfigure(0, weight=1)
                cell.grid_rowconfigure(0, weight=1)
                cell.grid_propagate(0)
                cell.grid(row=i + 1, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                # font = Font(size=FONT_SIZE, family=FONT_FAMILY, weight=FONT_WEIGHT)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, font=FONT)
                t.grid_propagate(0)
                t.grid(sticky="NESW")
                grid_row.append(t)

            self.grid_cells.append(grid_row)

        scoreCell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE / GRID_LEN, height=SIZE / GRID_LEN)
        scoreCell.grid_columnconfigure(0, weight=1)
        scoreCell.grid_rowconfigure(0, weight=1)
        scoreCell.grid_propagate(0)
        scoreCell.grid(row=0, column=0, columnspan=4, padx=GRID_PADDING, pady=GRID_PADDING, sticky='news')
        scoreText = Label(master=scoreCell, text="Score: " + str(self.totalScore), bg="#3C3738", fg="#BDC0BA", font=FONT)
        #scoreText.grid()
        scoreText.grid_propagate(0)
        scoreText.grid(sticky='news')
        self.mode_btn = tk.Button(text="Bot Play", width=BTN_WIDTH, command=self.toggle, font=("Verdana", 15, "bold"), bg="#3C3738",
                             fg="#BDC0BA")
        self.mode_btn.grid_propagate(0)
        self.mode_btn.grid(sticky=E + W, padx=GRID_PADDING, pady=GRID_PADDING)
        # global mode
        self.mode = True
        self.grid_cells.append(scoreText)

    def gen(self):
        return randint(0, GRID_LEN - 1)

    def init_matrix(self):
        self.matrix = new_game(4)

        self.matrix=add_two(self.matrix)
        self.matrix=add_two(self.matrix)


    def update_grid_cells(self,score):
        print(self.grid_cells[0][0].winfo_width())
        self.totalScore+=score
        self.grid_cells[-1].configure(text="Score: " + str(self.totalScore))
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg=BACKGROUND_COLOR_DICT[new_number], fg=CELL_COLOR_DICT[new_number])
        self.update_idletasks()
        print ("direction to follow ")

        ll=True
        if game_state(self.matrix) == 'win':
            ll=False
            self.grid_cells[1][1].configure(text="You", bg=BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_cells[1][2].configure(text="Win!", bg=BACKGROUND_COLOR_CELL_EMPTY)
        if game_state(self.matrix) == 'lose':
            ll=False
            self.grid_cells[1][1].configure(text="You", bg=BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_cells[1][2].configure(text="Lose!", bg=BACKGROUND_COLOR_CELL_EMPTY)

        # print("Mode - "  + str(mode))

        if(ll and self.mode):
            self.takeBotTurn()
        

    def takeBotTurn(self):
        k=direction(self.matrix)
        if(k=='left'):
            keybord.press('a')
        if (k == 'right'):
            keybord.press('d')
        if (k == 'up'):
            keybord.press('w')
        if (k == 'down'):
            keybord.press('s')


    def key_down(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix,done,score = self.commands[repr(event.char)](self.matrix)
            if done:
                self.matrix = add_two(self.matrix)
                self.update_grid_cells(score)
                done=False
                if game_state(self.matrix)=='win':
                    self.grid_cells[1][1].configure(text="You",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!",bg=BACKGROUND_COLOR_CELL_EMPTY)
                if game_state(self.matrix)=='lose':
                    self.grid_cells[1][1].configure(text="You",bg=BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!",bg=BACKGROUND_COLOR_CELL_EMPTY)


    def generate_next(self):
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2


    def toggle(self):
        # global mode
        if self.mode_btn.config('text')[-1] == 'Bot Play':
            self.mode_btn.config(text='Human Play')
            self.mode = False
        else:
            self.mode_btn.config(text='Bot Play')
            self.mode = True
            self.takeBotTurn()



gamegrid = GameGrid()
