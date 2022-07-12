import copy
import numpy as np
import time

def GetMoves():  # Create all the possible actions and create the state data
    possible_actions = np.array([('U', [0, 1, 2], -3), ('D', [6, 7, 8], 3), ('L', [0, 3, 6], -1), ('R', [2, 5, 8], 1)],
                                dtype=[('move', str, 1), ('position', list), ('head', int)])
    statetype = [('board', list), ('parent', int), ('gn', int), ('hn', int)]

    return possible_actions, statetype

#calculates the manhatten hueristic
def manhattan(board):
    return sum((abs(board // 3 - board // 3) + abs(board % 3 - board % 3))[1:])

def Priority_Queue(pri):
    pri = np.sort(pri, kind='mergesort', order=['f_value',
                                                    'position'])  # mergesort is used to traverse the list according to the lowest f_value
    pos, f_val = pri[0]  # get the lowest f_value and its position from que
    pri = np.delete(pri, 0, 0)  # remove what we are exploring

    return pri, pos, f_val

#calculates the misplaced tiles hueristic
def misplacedtiles(board, goal_s):
    board = board.reshape((3,3))
    goal_s = goal_s.reshape((3,3))
    count = 0
    for i in range(3):
        for j in range(3):
             if (board[i][j]!=0 and board[i][j]!= goal_s[i][j]):
                count+=1
    return count

#check if already traversed
def all(checklist):
    set=[]
    for list in set:
        for checklist in list:
            return True
        else:
            return False

def calculate_A(board, goal, heuristic):
    pa, sv = GetMoves()  # Get all possible actions aswell as the type of the type of the data kept

    parent = -1  # initializing the initial state (s0)
    g_value = 0
    h_value = 0

    if (heuristic):  # get the value of h depending on what the user has chosen
        h_value = manhattan(board)
    else:
        h_value = misplacedtiles(board, goal)

    state = np.array([(board, parent, g_value, h_value)],
                     sv)  # calculate state which contains the board config, which parent(since no parent marked -1) and g and f

    priority = np.array([(0, h_value)], [('position', int), (
    'f_value', int)])  # initiliziation of priority queue since f = g + h and g = 0, only h is passed.

    if np.array_equal(board, goal):  # if goal state has been found initially
        return state, len(priority)

    while True:  # infinite loop to allow the retrival of the states

        priority, position, f_value = Priority_Queue(priority)  # call the priority queue
        board, parent, g_value, h_value = state[position]  # retrieve the states data

        g_value += 1  # new 'level'

        # get the position of the empty space
        get_pos = int(np.where(board == 0)[0])

        for actions in pa:  # get all possible actions from possible actions
            if get_pos not in actions['position']:
                board_copy = copy.copy(board)  # create a new list which is a copy of the old list
                board_copy[get_pos], board_copy[get_pos + actions['head']] = board_copy[get_pos + actions['head']], \
                                                                             board_copy[
                                                                                 get_pos]  # apply the action to the board copy

                if ~(np.all(list(state['board']) == board_copy,
                            1)).any():  # check to not traverse what has already been traversed

                    # calls either the manhatten or the misplacedtiles hueristic for the new state
                    if (heuristic):
                        h_value = manhattan(board_copy)
                    else:
                        h_value = misplacedtiles(board_copy, goal)

                        # add new state in the list
                    new_state = np.array([(board_copy, position, g_value, h_value)], sv)
                    state = np.append(state, new_state, 0)

                    f_value = g_value + h_value  # calculate the new state f by f = g + h

                    new_state = np.array([(len(state) - 1, f_value)], [('position', int), ('f_value', int)])
                    priority = np.append(priority, new_state, 0)  # append the new state to the priority que

                    if np.array_equal(board_copy, goal):  # if goal state has been found
                        return state, len(priority)


def evaluate_path(state):
    path = np.array([], int).reshape(-1, 9) #create an empty list
    traversal = len(state) - 1
    while traversal != -1: #while we havent reached parent
        path = np.insert(path, 0, state[traversal]['board'], 0)
        traversal = (state[traversal]['parent'])
    return path.reshape(-1, 3, 3) #convert back to matrix

#counts the number of inverstions to check whether odd or even for validity
def inversions(board):
    count = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if board[j] != 0 and board[i] != 0 and board[i] > board[j]:
                count += 1
    return count

def Astar():
    initial = np.array(list(map(int, input('Enter board (sample input 123405678): '))))  # sample input 123405678
    goal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])

    if sorted(initial) != sorted([0, 1, 2, 3, 4, 5, 6, 7, 8]):  # check if user entered inputs correctly
        print('incorrect input')
        return

    if inversions(initial) % 2:  # validation check using inversions
        print('Not Valid')
        return

    n = int(input("1. Manhattan distance \n2. Misplaced tiles\n"))

    state = []
    visited = 0

    if (n == 1):  # get what hueristic the user wants to use
        start = time.time()  # starts the time for the algorithm
        state, visited = calculate_A(initial, goal, True)
    elif (n == 2):
        start = time.time()
        state, visited = calculate_A(initial, goal, False)
    else:
        print('incorrect input')
        return

    path = evaluate_path(state)  # evaluates the best path to the goal state

    end = time.time()
    print(str(path))
    totalactions = len(path) - 1
    print('Valid')
    print(f'Runtime of algorithm is {end - start}')
    print('Number of actions:', totalactions)
    print('The total number of unique states generated', len(state))
    visit = len(state) - visited
    print('Total number of unique states visited:', visit, "\n")

    return

Astar()
input("Press enter to exit")