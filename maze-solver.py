import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    GREEN = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, 2*j, 'X', RED)
            else:    
                stdscr.addstr(i, 2*j, value, GREEN)

def find_start(maze, start):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == start:
                return i, j
    
    return None

def find_path(maze, stdscr):
    start = 'O'
    end = 'X'
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.4)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbours = find_neighbours(maze, row, col)
        for neighbour in neighbours:
            if neighbour in visited:
                continue

            r, c = neighbour

            if maze[r][c] == '#':
                continue
                
            new_path = path + [neighbour]
            q.put((neighbour, new_path))
            visited.add(neighbour)


        
def find_neighbours(maze, row, column):
    neighbours = []

    if row > 0: #UP
        neighbours.append((row - 1, column))
    
    if row + 1 < len(maze): #DOWN
        neighbours.append((row + 1, column))
    
    if column > 0: #LEFT
        neighbours.append((row, column - 1))

    if column + 1 < len(maze[0]): #RIGHT
        neighbours.append((row, column + 1))

    return neighbours
    


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    

    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)