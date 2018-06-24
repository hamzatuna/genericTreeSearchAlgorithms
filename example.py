import time
import os
from generics.generic import  bfs, dfs, astar

MOVES = [ #Right,Left,Down,Up
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]
G = [[0, 1, 0, 1, 0, 0 ], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0]]

def main():
    #Start [0,0] , End [n-1,m-1]
    start = (0,0)
    end = (len(G)-1, len(G[0])-1)
    h = lambda point: sum(x-y for x,y in zip(end, point))
    A = astar(start, end, h)

    print('astart path:', A.search(PossiblePoints))
    print('astar cost of end', A.cost[end])

    B = bfs(start, end)

    print('bfs path:', B.search(PossiblePoints))
    print('bfs cost of end', B.cost[end])

    D = dfs(start, end)

    print('dfs path:', D.search(PossiblePoints))
    print('dfs cost of end', D.cost[end])

def isValid(point):
    return 0<=point[0]<len(G) and 0<=point[1]<len(G[0])  and (not G[point[0]][point[1]])

def PossiblePoints(current_point): #The points that provide the conditions and can be reached from the point we are on now
    near_points = [(current_point[0]+x, current_point[1]+y) for x,y in MOVES] # Gets all adjacent points(Up,Down,Right,Left)
    return list(filter(lambda point: isValid(point), near_points)) #Filters adjacent points and returns the points that provide the conditions.

if __name__ == "__main__":
    main() 

