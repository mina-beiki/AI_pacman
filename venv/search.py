# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    #Each successor is a tuple, first argument is the state and the second one is the action
    stack = util.Stack()
    start = problem.getStartState()
    state = start #to use it in while loop
    stack.push((start, []))
    path = []
    while not stack.isEmpty() and not problem.isGoalState(state):
        #print(problem.isGoalState(state))
            s, action = stack.pop()
            #print("\n", action)
            path.append(s)
            #print("processing: ", s)
            for adj in problem.getSuccessors(s):
                place = adj[0]
                if not place in path: #make sure it's not already visited
                    dir = adj[1]
                    state = place
                    #print("dir: \n",dir)
                    #print("state: \n",place)
                    stack.push( (place, action + [dir] )) #everytime it appends the new action
    print(action)
    return action + [dir]
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # Each successor is a tuple, first argument is the state and the second one is the action
    queue = util.Queue()
    start = problem.getStartState()
    state = start  # to use it in while loop
    queue.push((start, []))
    visited = []
    visited.append(start)
    while not queue.isEmpty() :
        s, action = queue.pop()
        if problem.isGoalState(s):
            #print("goal!")
            #print(action)
            return action
        # print("\n", action)
        # print("processing: ", s)
        for adj in problem.getSuccessors(s):
            place = adj[0]
            if not place in visited:  # make sure it's not visited
                visited.append(place)
                #print("visited = ", visited)
                dir = adj[1]
                state = place
                #print("dir: ",dir)
                #print("\nstate: ",place)
                queue.push((place, action + [dir]))  # everytime it appends the new action
    return action
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # Each successor is a tuple, first argument is the state and the second one is the action
    queue = util.PriorityQueue()
    start = problem.getStartState()
    state = start  # to use it in while loop
    queue.push((start, []), 0)
    visited = []
    while not queue.isEmpty() :
        s, action = queue.pop()
        # print("\n", action)
        # print("processing: ", s)
        if problem.isGoalState(s):
            return action
        #if we don't put this if here, we will have many repeated nodes.
        if s not in visited:
            for adj in problem.getSuccessors(s):
                place = adj[0]
                if place not in visited:  # make sure it's not visited
                    dir = adj[1]
                    state = place
                    # print("dir: \n",dir)
                    # print("state: \n",place)
                    queue.push((place, action + [dir]), problem.getCostOfActions(action + [dir] ) )  # everytime it appends the new action
        visited.append(s)
    print(action)
    return action
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    queue = util.PriorityQueue()
    start = problem.getStartState()
    state = start  # to use it in while loop
    queue.push((start, []), 0 + heuristic(start, problem))
    visited = []
    while not queue.isEmpty() :
        s, action = queue.pop()
        # print("\n", action)
        # print("processing: ", s)
        if problem.isGoalState(s):
            return action
        #if we don't put this if here, we will have many repeated nodes.
        if s not in visited:
            for adj in problem.getSuccessors(s):
                place = adj[0]
                if not place in visited:  # make sure it's not visited
                    dir = adj[1]
                    state = place
                    # print("dir: \n",dir)
                    # print("state: \n",place)
                    queue.push((place, action + [dir]), heuristic(place, problem) + problem.getCostOfActions(action + [dir] ) )  # f = h + g
        visited.append(s)
    print(action)
    return action
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
