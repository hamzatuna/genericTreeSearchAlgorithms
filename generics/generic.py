
from collections import defaultdict, deque

MOVES = [ #Right,Left,Down,Up
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

class bfs: 
    def __init__(self, start, end):
        self.start = start
        self.end = end


    def search(self, nextPointsFunction, parent={}):
        # deque can add and pop boths side of lists with O(1) time complexity
        d = deque()
        visited = defaultdict(int)
        
        # add start point 
        d.append(self.start)
        
        while len(d) > 0:
            current_point = d.popleft()
            # check solution is found
            if current_point == self.end:
                return self.get_path(parent, current_point)

            # get next points
            new_points = nextPointsFunction(current_point)
            # discard visited points
            not_visited_points = filter(lambda p: not visited[p], new_points)

            for point in not_visited_points:
                parent[point] = current_point
                visited[point] = 1
                d.append(point)

    def get_path(self, parent, current_point):
        path = [current_point]

        while current_point != self.start:
            current_point = parent[current_point]
            path.append(current_point)
        
        path.reverse()
        return path