# Generic Tree Search Algorithms
Generic classes/functions are implamented for dynamic use of tree search algorithms. BFS, DFS and A* are added untill now.

### Examples

### Rat in Maze

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
#### A* solution
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
print('astart path:', astar.search(moves))
# cost attribute is created after search operation
print('astar cost of end', astar.cost[end])
```
#### BFS solution
```
bfs = BFS(start, end)

print('bfs path:', bfs.search(moves))
print('bfs cost of end', bfs.cost[end])
```
#### DFS solution
```
dfs = DFS(start, end)

print('dfs path:', dfs.search(moves))
print('dfs cost of end', dfs.cost[end])
```

