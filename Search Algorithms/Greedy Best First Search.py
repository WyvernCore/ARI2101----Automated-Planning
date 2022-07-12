import sys
import copy
import time
import numpy as np

class Node:    
    def __init__(self,start=None,d=None,path=None,move=None,h=None):
        self.state=start
        self.depth=d
        self.currPath=path
        self.movement=move
        self.hValue=h

    #finding the position of the blank variable, placing it into global variable
    def findBlank(self, currentGrid):
        global curBlank
        checkBlank = None
        for y in range(0,3):
            for x in range(0,3):
                if(currentGrid.state[y][x]==0 ):
                    curBlank = (y,x)
                    break
            if checkBlank != None:
                break

    #generating and returning nextState of a state with moves in 4 directions
    def movementOptions(self,currState,visited,h=None,totalNodes=None):
        nextState=[]
        
        self.findBlank(currState)
        
        #uses the global variable and takes the y and x positions of it for the next step
        curY = curBlank[0]
        curX = curBlank[1]

        if (curY-1 >= 0):  #if not top row, move up
            finalPath = copy.deepcopy(currState.currPath)       
            finalPath.append("UP")
            child = Node(copy.deepcopy(currState.state), currState.depth + 1,finalPath, "UP",h)
            child.state[curY-1][curX], child.state[curY][ curX] = child.state[curY][curX], child.state[curY-1][curX]
            if (self.toString(child.state) not in visited):
                nextState.append(child)
                totalNodes+=1

        if (curY+1 <= 2):  #if not bottom row, move down
            finalPath = copy.deepcopy(currState.currPath)
            finalPath.append("DOWN")
            child = Node(copy.deepcopy(currState.state), currState.depth + 1, finalPath, "DOWN",h)
            child.state[curY + 1][curX], child.state[curY][curX] = child.state[curY][curX], child.state[curY + 1][curX]
            if (self.toString(child.state) not in visited):
                nextState.append(child)
                totalNodes+=1

        if (curX-1 >= 0) : #if not left-most column, move left
            finalPath=copy.deepcopy(currState.currPath)
            finalPath.append("LEFT")
            child=Node(copy.deepcopy(currState.state),currState.depth+1,finalPath,"LEFT",h)
            child.state[curY][curX-1],child.state[curY][curX]=child.state[curY][curX],child.state[curY][curX-1]
            if (self.toString(child.state) not in visited):
                nextState.append(child)
                totalNodes+=1

        if (curX+1 <= 2):  #if not right-most column, move right
            finalPath = copy.deepcopy(currState.currPath)
            finalPath.append("RIGHT")
            child = Node(copy.deepcopy(currState.state), currState.depth + 1,finalPath, "RIGHT",h)
            child.state[curY][curX+1], child.state[curY][ curX] = child.state[curY][curX], child.state[curY][curX+1]
            if (self.toString(child.state) not in visited):
                nextState.append(child)
                totalNodes+=1

        return nextState,totalNodes

       


    #Converting the state to a string so it can be stored in the set
    #to compare to 'visited'
    def toString(self,tmpState):
        s=''
        for i in tmpState:
            for j in i:
                s+=str(j)
        return s

    #Calculating manhatten heuristic value
    def manhatten(self,state):
        hVal = 0
        goalY = [1, 0, 0, 0, 1, 2, 2, 2, 1]
        goalX = [1, 0, 1, 2, 2, 2, 1, 0, 0]

        #go through current state, find dist.
        for i in range(0, 3):
            for j in range(0,3):
                temp = i
                al_temp = j
                num=state[temp][al_temp]  

                #skips if current node == blank
                if(num!=0):
                    hVal += abs(i-goalY[num])+abs(j-goalX[num]) # hVal = addition of how far all the numbers are from their goal state
        return hVal

    #Calculating displaced tile heuristic value
    def misplacedTiles(self,state):
        hVal=0
        for i in range(0,3):
            for j in range(0,3):
                if (state[i][j] != 0):
                    if(state[i][j]!=goalState[i][j]):
                        hVal+=1
        return hVal


 
    def greedybfs(self, numOption):
        maxListsize = -sys.maxsize - 1  #largest value a list can store, used to avoid crash
        startList = []      #holds the starting state, so that it can be worked on
        totalNodes=0
        isSolved = False
        #variables to do with time
        timeFlag=0
        startTimer = time.time()
        
        #goalReached = 0        #acts as a switch - break the loop below when goal == reached

        visited = set()        #set of all the states visited

        #check for heuristic
        #startNode = hVal, depth
        if(numOption == 1):
            startNode = Node(startState, 1, [],'',self.manhatten(startState))
        elif(numOption == 2):
            startNode = Node(startState, 1, [],'',self.misplacedTiles(startState))
        startList.append(startNode)

        while(startList):
            #change to max (runtime error)
            if len(startList)>maxListsize:
                maxListsize=len(startList)
            #time
            temp_time = time.time()
            if (temp_time - startTimer >= 10 * 60):
                timeFlag = 1
                break

            startList.sort(key=lambda x: x.hValue) 
            currentNode= startList.pop(0)
            stateString = self.toString(currentNode.state)
            visited.add(stateString)
            
            #Reached goal state (output)
            if (currentNode.state == goalState):
                print ("Moves: "+str(len(currentNode.currPath)))
                print("Each move represents where the blank(0) went")
                print  (str(currentNode.currPath))
                print()
                isSolved = True
                goalReached = 1 #make it act like a switch
                print ("Nodes visited: " + str(totalNodes))
                if(numOption == 1):
                     print ("Time: "+ str(time.time()-startTimer))
                elif(numOption == 2):
                     print ("Time: "+ str(time.time()-startTimer))
                     print ("Max List Size="+str(maxListsize))

            #solved
            if isSolved:
                break   

            if(numOption == 1):
                totalChildren,totalNodes=self.movementOptions(currentNode,visited,self.manhatten(currentNode.state),totalNodes)

            elif(numOption == 2):
                totalChildren,totalNodes=self.movementOptions(currentNode,visited,self.misplacedTiles(currentNode.state),totalNodes)

            startList.extend(totalChildren)# Adding the expanded chidrens to the list
        if timeFlag == 1:
            print ("No. of nodes visited: " + str(totalNodes))
            print("No solution found before algorithm timed out")

initial = list(map(int, input('Enter board (sample input 123405678): ')))
initial = np.array(initial)

startState = initial.reshape(3,3).tolist()
#startState = [[8, 6, 7], [2, 5, 4], [3, 0, 1]]
goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def main():

    print ("Greedy Best First Search")

    print ("1. Manhatten Heuristic")
    print ("2. Misplaced Tile Heuristic")
    methodChosen = int(input())
    print("-------------------------------")


    struct = Node()         #calling the node structure
    if methodChosen == 1:
        struct.greedybfs(methodChosen)
    elif methodChosen == 2:
        struct.greedybfs(methodChosen)
 

main()
input("Press enter to exit")