"""
 This program simulates cell-like creatures living and
 dying in a grid based on the classic simulation
 Conway's Game of Life.

 Each cell starts off either living or dead based on a
 random probability. From there, the cells live and die
 with each tick in time, based on the following model:

 If  a cell has --
 fewer than 2 live neighbors: cell dies
 2 neighbors: cell stays the way it is
 3 neighbors: cell is born
 4 or more neighbors: cell dies of overcrowding

 Try manipulating the constants below and see how the
 simulation changes!
"""
from tkinter import *
import random
import time

DELAY = .200
ALIVE = 1
DEAD = 0
NUM_COLS = 50
NUM_ROWS = 50
BOX_SIZE = 5
LIFE_PROB = 0.5
WIDTH = NUM_COLS * BOX_SIZE
HEIGHT = NUM_ROWS * BOX_SIZE

root = Tk()

screen = Canvas(root, width=WIDTH, height=HEIGHT, background="white")
screen.pack()

grid = [[0 for x in range(NUM_COLS)] for y in range(NUM_ROWS)]
screen_grid = [[0 for x in range(NUM_COLS)] for y in range(NUM_ROWS)]

# takes an int that represents the status
# of a cell and returns the corresponding color
# ALIVE returns BLACK
# DEAD returns WHITE
def get_color(status):
    if status == 0:
        return "white"
    else:
        return "black"

# returns a boolean that represents
# whether a row number is within the grid
def row_in_bounds(row):
    if row < 0:
        return False
    if row >= NUM_ROWS:
        return False
    return True

# returns a boolean that represents
# whether a row number is within the grid
def col_in_bounds(column):
    if column < 0:
        return False
    if column >= NUM_COLS:
        return False
    return True

# returns the number of live neighbors a cell has
# not counting itself
def num_neighbors(row, column):
    num_neighbors = 0
    for delta_i in range(-1, 2, 1):
        for delta_j in range(-1, 2, 1):
            neighbor_row = row-delta_i
            neighbor_col = column-delta_j
            if row_in_bounds(neighbor_row) and col_in_bounds(neighbor_col):
                if neighbor_row != row or neighbor_col != column:
                    num_neighbors += grid[neighbor_row][neighbor_col]
    return num_neighbors

# takes a current grid and returns a grid with
# the next generation of cells based on the rules
# fewer than 2 live neighbors: cell dies
# 2 neighbors: cell stays the way it is
# 3 neighbors: cell is born
# 4 or more neighbors: cell dies of overcrowding
def compute_next_grid(grid):
    new_grid = [[0 for x in range(NUM_COLS)] for y in range(NUM_ROWS)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbors = num_neighbors(i, j)
            if neighbors < 2:
                new_grid[i][j] = DEAD
            if neighbors == 2:
                new_grid[i][j] = grid[i][j]
            if neighbors == 3:
                new_grid[i][j] = ALIVE
            if neighbors > 3:
                new_grid[i][j] = DEAD
    return new_grid

# Generates a grid of cells with
# randomly assigned life
def init_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            is_alive = random.random()
            if is_alive <= LIFE_PROB:
                grid[i][j] = 1
            else:
                grid[i][j] = 0

def init_screen_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            is_alive = grid[i][j]
            screen_grid[i][j] = screen.create_rectangle(BOX_SIZE*i, BOX_SIZE*j, \
                BOX_SIZE*(i+1), BOX_SIZE*(j+1), fill=get_color(is_alive), outline="")
    screen.update()
    
# displays a grid of rectangles that represents
# the contents of the grid parameter.
# live cells are represented as black rectangles
# dead cells are white rectangles
def update_grid():
    global grid
    grid = compute_next_grid(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            is_alive = grid[i][j]
            screen.itemconfig(screen_grid[i][j], fill=get_color(is_alive))
    screen.update()

init_grid(grid)
init_screen_grid(grid)
while True:
    update_grid()
    time.sleep(DELAY)
mainloop()
