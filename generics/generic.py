
from collections import defaultdict, deque

class generic_search:
    def __init__(self, start, end):
        self.start = start
        self.end = end


    def search(self, nextPointsFunction, parent={}):
        d = self._get_ds()
        visited = defaultdict(int)
        
        # add start point 
        self._add_point(d, self.start)
        
        while len(d) > 0:
            current_point = self._get_next_item(d)

            # check solution is found
            if current_point == self.end:
                return self.get_path(parent, current_point)

            # get next points
            new_points = self._get_new_points(current_point, nextPointsFunction)
            # discard visited points
            not_visited_points = filter(lambda p: not visited[p], new_points)

            for point in not_visited_points:
                parent[point] = current_point
                visited[point] = 1
                self._add_point(d, point)
    


    def get_path(self, parent, current_point):
        path = [current_point]

        while current_point != self.start:
            current_point = parent[current_point]
            path.append(current_point)
        
        path.reverse()
        return path

class bfs(generic_search): 

    def _get_ds(self):
        return deque()
    
    def _get_next_item(self, ds):
        return ds.popleft()
    
    def _add_point(self, ds, item):
        ds.append(item)

    def _get_new_points(self, current_point, nextPointsFunction):
        return nextPointsFunction(current_point)
    
class dfs(generic_search): 
    
    def _get_ds(self):
        return deque()
    
    def _get_next_item(self, ds):
        return ds.pop()
    
    def _add_point(self, ds, item):
        ds.append(item)
    
    def _get_new_points(self, current_point, nextPointsFunction):
        return nextPointsFunction(current_point)