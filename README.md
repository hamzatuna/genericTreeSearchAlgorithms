# Generic Tree Search Algorithms
Generic classes/functions are implamented for dynamic use of tree search algorithms. BFS, DFS and A* are added untill now.

## Examples

###  1-) Rat in Maze

You have maze as matrix: 

```
G = [
        [0, 1, 0, 1, 0, 0], 
        [0, 1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 1, 0], 
        [0, 0, 0, 1, 1, 0]
    ]
```
You have start point and end point. And You want to go to end point from end point.
```
#Start [0,0] , End [n-1,m-1]
start = (0,0)
end = (len(G)-1, len(G[0])-1)
```
#### A* solution
```
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
path = astar.search(moves)
# cost attribute is created after search operation
cost = astar.cost[end]
```
##### BFS solution
```
bfs = BFS(start, end)

path = bfs.search(moves))
cost = bfs.cost[end]
```
##### DFS solution
```
dfs = DFS(start, end)

path = dfs.search(moves)
cost = dfs.cost[end])
```

###  2-) KnightL on Chessboard
Hackerrank quention [link](https://www.hackerrank.com/challenges/knightl-on-chessboard/problem):

 Knight is a chess piece that moves in an L shape. We define the possible moves of  as any movement from some position  to some  satisfying either of the following:
 * x2 = +-a and y2 = +-b, or
 * x2 = +-b and y2 = +-a

Note that  and  allow for the same exact set of movements. For example, the diagram below depicts the possible locations that  or  can move to from its current location at the center of a  chessboard:

![image of chess moves](https://s3.amazonaws.com/hr-assets/0/1486410238-98ef4547f1-knightl-example-ps.png)
####   Solution with using BFS:

```
moves = [
    (1,1), 
    (-1, 1), 
    (1, -1), 
    (-1, -1)]

# function clousure to generate nextMoves
def get_next_pointF(pos, n):

    def nextMoves(point):
        all_moves = ([(point[0] + pos[0]*move[0], point[1] + pos[1]*move[1]) 
                for move in moves] + 
            [(point[0] + pos[1]*move[0], point[1]+pos[0]*move[1]) 
                for move in moves])

        filtered_moves = filter(lambda move: 0<=move[0]<n and 
                    0<=move[1]<n, all_moves)
        
        return set(filtered_moves)
    return nextMoves

def get_dis_matrix(n):
    start = (0,0)
    end = (n-1, n-1)
    b = BFS(start, end)
    
    results = [[-1 for i in range(1, n)] for j in range(1, n)]
    
    for i in range(1, n):
        for j in range(i, n):
            nextMoves = get_next_pointF((i, j), n)
            path = b.search(nextMoves)

            if path:
                results[i-1][j-1] = len(path)-1
                results[j-1][i-1] = len(path)-1

    return results
```