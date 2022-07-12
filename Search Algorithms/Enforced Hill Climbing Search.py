from random import choice
from time import time
import numpy as np

# Boards, 0 used for empty space
def EFHC():
    initial = (list(map(int, input('Enter board (sample input 123405678): '))))  # sample input 123405678
    initial = np.array(initial)

    BOARD = initial.reshape((3,3)).tolist()
    if __name__ == "__main__":
        heuristic = input("Manhattan distance (1) or misplaced tiles (2)? ")
        t = solve(BOARD, manhattan_distance if heuristic == "1" else misplaced_tiles)
        print(f"Time: {t} seconds")



def misplaced_tiles(board):
    count = 0
    for x in range(3):
        for y in range(3):
            i = board[y][x]
            if i != 0 and i != y*3 + x + 1:
                count += 1
    return count

def manhattan_distance(board):
    distance = 0
    for x in range(3):
        for y in range(3):
            i = board[y][x]
            if i != 0:
                X, Y = (i-1) % 3, (i-1) // 3
                distance += abs(X - x) + abs(Y - y)
    return distance

#copies the exact formation of the board (as a 2D List)
def deep_copy(board):
    return [row[:] for row in board]

#convert current state of the board to string
def toString(board):
    return "".join(str(i) for row in board for i in row)        

def solve(initial_board, heuristic):
    x, y = 0, 0
    for X in range(3):
        for Y in range(3):
            if initial_board[Y][X] == 0:
                x, y = X, Y

    board = deep_copy(initial_board)
    h = heuristic(board)
    history = {}
    total_states = 0
    move_count = 0
    start = time()
    while h > 0:
        history[toString(board)] = True
        move_count += 1
        moves = []
        states = 0
        if x > 0:
            states += 1
            new_board = deep_copy(board)
            new_board[y][x], new_board[y][x-1] = new_board[y][x-1], new_board[y][x]
            moves.append(("Left ", heuristic(new_board), new_board, -1, 0))
        if x < 2:
            states += 1
            new_board = deep_copy(board)
            new_board[y][x], new_board[y][x+1] = new_board[y][x+1], new_board[y][x]
            moves.append(("Right", heuristic(new_board), new_board, 1, 0))
        if y > 0:
            states += 1
            new_board = deep_copy(board)
            new_board[y][x], new_board[y-1][x] = new_board[y-1][x], new_board[y][x]
            moves.append(("Up   ", heuristic(new_board), new_board, 0, -1))
        if y < 2:
            states += 1
            new_board = deep_copy(board)
            new_board[y][x], new_board[y+1][x] = new_board[y+1][x], new_board[y][x]
            moves.append(("Down ", heuristic(new_board), new_board, 0, 1))
        filtered_moves = list(filter(lambda move: not history.get(toString(move[2])), moves))
        move = None
        if len(filtered_moves) == 0:
            move = choice(moves)
        else:
            move = sorted(filtered_moves, key=lambda move: move[1])[0]
        h = move[1]
        board = move[2]
        x += move[3]
        y += move[4]
        print(f"Move {move[0]}  States: {states}")
        total_states = total_states + states
    print(f"\nDone. Total moves: {move_count}")
    print(f"\nTotal states generated: {total_states}")
    print(board)
    end = time()
    return end-start



EFHC()
input("Press enter to exit")
