import time
import queue
import numpy as np

class Board:
    totalstates = 0

    def __init__(self, state, parent, action):  # keeps track of all states
        self.parent = parent
        self.state = state
        self.action = action
        Board.totalstates += 1  # appends to total state everytime board is called

    def getSolution(self):  # traversing back to get what soultion has been found.
        solution = []
        solution.append(self.state)  # add solution to list
        path = self
        while (path.parent != None):  # while parent hasn't been reached
            path = path.parent
            solution.append(path.state)  # add solution to list
        solution.reverse()  # reverse soultion for output
        return solution

    def generate_child(self):
        child_state = []
        blank_location = self.state.index(0)  # find where 0 is located in array
        row = int(blank_location / 3)
        column = int(blank_location % 3)

        pa = GetMoves(row, column)

        for action in pa:
            board_copy = self.state.copy()  # create a copy of the board
            if action == 'U':  # shift blank up
                board_copy[blank_location], board_copy[blank_location - 3] = board_copy[blank_location - 3], board_copy[blank_location]
            elif action == 'D':  # shift blank down
                board_copy[blank_location], board_copy[blank_location + 3] = board_copy[blank_location + 3], board_copy[blank_location]
            elif action == 'L':  # shift blank left
                board_copy[blank_location], board_copy[blank_location - 1] = board_copy[blank_location - 1], board_copy[blank_location]
            elif action == 'R':  # shift blank right
                board_copy[blank_location], board_copy[blank_location + 1] = board_copy[blank_location + 1], board_copy[blank_location]
            child_state.append(Board(board_copy, self, action))
        return child_state

def goalfound(board):
    goal=[1,2,3,4,5,6,7,8,0]
    if (board == goal):
        return True
    return False

def GetMoves(row, column):
    possiblemoves = ['U', 'D', 'L', 'R']
    if (column == 0):
        possiblemoves.remove('L')
    elif (column == 2):
        possiblemoves.remove('R')
    if (row == 0):
        possiblemoves.remove('U')
    elif (row == 2):
        possiblemoves.remove('D')

    return possiblemoves

def calculate_BFS(initial_state):
    start_node = Board(initial_state, None, None)

    if goalfound(initial_state):  # check if initial is goal
        return start_node.getSolution()

    states = queue.Queue()  # create a queue to keep track of the states
    states.put(start_node)
    explored = []

    while not (states.empty()):
        node = states.get()
        explored.append(node.state)  # keep track of what has been explored
        board_copy = node.generate_child()  # create a new child to traverse
        for child in board_copy:  # go over every child in new depth
            if child.state not in explored:  # if the child in depth hasnt been explored proceed
                if goalfound(child.state):
                    return child.getSolution()  # if a solution is found ge the solution
                states.put(child)
    return

#counts the number of inverstions to check whether odd or even for validity
def inversions(board):
    count = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if (board[j] != 0 and board[i] != 0 and board[i] > board[j]):
                count += 1
    return count


def bfs():
    initial = list(map(int, input('Enter board (sample input 123405678): ')))  # sample input 123405678
    if sorted(initial) != sorted([0, 1, 2, 3, 4, 5, 6, 7, 8]):  # check if user entered inputs correctly
        print('incorrect input')
        return

    if inversions(initial) % 2:  # validation check using inversions
        print('Not Valid')
        return

    start = time.time()  # starts the time for the algorithm
    Board.totalstates = 0
    bfs = calculate_BFS(initial)
    end = time.time()
    totalactions = len(bfs)

    bfs = np.array(bfs)  # transform solution to 3x3 matrix
    for i in range(len(bfs)):
        print(bfs[i].reshape((3, 3)))
        print()

    print('Valid')
    print(f'Runtime of algorithm is {end - start}')
    print('Number of actions:', totalactions)
    print('The total number of unique states generated', Board.totalstates)

bfs()
input("Press enter to exit")