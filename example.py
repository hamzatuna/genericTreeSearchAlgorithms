import time
import os
from generics import  BFS, DFS, AStar

MOVES = [ #Right,Left,Down,Up
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]


# graph
G = [
        [0, 1, 0, 1, 0, 0], 
        [0, 1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 1, 0], 
        [0, 0, 0, 1, 1, 0]
    ]

def main():
    # Start [0,0] , End [n-1,m-1]
    start = (0,0)
    end = (len(G)-1, len(G[0])-1)

    # heuristic function
    # takes only current point 
    # and return heuristic value of current point
    h = lambda point: sum(x-y for x,y in zip(end, point))

    # create Astart instance 
    # with starr point, end point and heuristic function
    astar = AStar(start, end, h)

    # search method returns path
    print('astart path:', astar.search(moves))
    # cost attribute is created after search operation
    print('astar cost of end', astar.cost[end])

    # BFS
    bfs = BFS(start, end)
    
    print('bfs path:', bfs.search(moves))
    print('bfs cost of end', bfs.cost[end])

    dfs = DFS(start, end)

    print('dfs path:', dfs.search(moves))
    print('dfs cost of end', dfs.cost[end])

def isValidMove(point):
    return 0<=point[0]<len(G) and 0<=point[1]<len(G[0]) and (not G[point[0]][point[1]])

def moves(current_point): #The points that provide the conditions and can be reached from the point we are on now
    near_points = [(current_point[0]+x, current_point[1]+y) for x,y in MOVES] # Gets all adjacent points(Up,Down,Right,Left)
    return list(filter(lambda point: isValidMove(point), near_points)) #Filters adjacent points and returns the points that provide the conditions.

if __name__ == "__main__":
    main() 

