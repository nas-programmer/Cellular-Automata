"""Conway's Game of Life"""

import pygame, sys, random, numpy as np

size = (width, height) = 600, 350

pygame.init()

win = pygame.display.set_mode(size)
clock = pygame.time.Clock()

s = 10
cols, rows = int(win.get_width()/s), int(win.get_height()/s)

grid = []
for i in range(rows):
    arr = []
    for j in range(cols):
        arr.append(random.randint(0, 1))
    grid.append(arr)

def count(grid, x, y):
    c = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (y+j+cols)%cols
            row = (x+i+rows)%rows
            c += grid[row][col]
    c -= grid[x][y]
    return c

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    win.fill((0, 0, 0))

    for i in range(cols):
        for j in range(rows):
            x = i * s
            y = j * s
            if grid[j][i] == 1:
                pygame.draw.rect(win, (255, 255, 255), (x, y, s, s))
            elif grid[j][i] == 0:
                pygame.draw.rect(win, (0, 0, 0), (x, y, s, s))
            pygame.draw.line(win, (20, 20, 20), (x,y), (x, height))
            pygame.draw.line(win, (20, 20, 20), (x,y), (width,y))
    
    new_grid = []
    for i in range(rows):
        arr = []
        for j in range(cols):
            arr.append(0)
        new_grid.append(arr)

    
    for i in range(cols):
        for j in range(rows):
            neighbors = count(grid, j, i)
            state = grid[j][i]
            if state == 0 and neighbors == 3 :
                new_grid[j][i] = 1
            elif state == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[j][i] = 0
            else:
                new_grid[j][i] = state

    grid = new_grid

    pygame.display.flip()
