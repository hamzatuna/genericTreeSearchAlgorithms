
from collections import defaultdict, deque
from heapq import heappop, heappush
import operator

          
class generic_search:
    def __init__(
        self, 
        start, 
        end, 
        costF=lambda point, 
            pre_point, pre_point_cost: pre_point_cost+1):
        
        self.start = start
        self.end = end
        self.costF = costF
        self.get_point_from_item = lambda x: x

    def search(self, nextPointsFunction, parent={}):
        d = self._get_ds()
        visited = defaultdict(int)
        cost = {}
        
        self.parent = parent
        self.cost = cost
        
        cost[self.start] = 0
        
        # add start point 
        self._add_point(d, self.start)


        while len(d) > 0:
            current_item = self._get_next_item(d)
            current_point = self.get_point_from_item(current_item)
            cur_cost = cost[current_point]

            # check solution is found
            if current_point == self.end:
                return self.get_path(parent, current_point)

            # get next points
            new_points = nextPointsFunction(current_point)

            # update costs of points 
            for point in new_points:
                cost[point] = min(self.costF(point, current_point, cur_cost), 
                        cost.get(point, float('inf')))

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

class astar(generic_search):
    
    def __init__( 
        self, 
        start, 
        end,
        h,
        costF=lambda point, 
            pre_point, pre_point_cost: pre_point_cost+1):

        self.start = start
        self.end = end
        self.h = h
        self.costF = costF
        self.get_point_from_item = operator.itemgetter(1)

    
    def _get_ds(self):
        return []

    def _get_next_item(self, ds):
        return heappop(ds)

    def _add_point(self, ds, point):
        # points will be added as tuple of heuristic and data
        item_cost = self.cost[point]
        item_h = self.h(point)
        ds.append((item_cost+item_h, point))
    
    def _get_new_points(self, current_item, nextPointsFunction):
        return nextPointsFunction(current_item[1])