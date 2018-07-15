from generics import DFS

moves = [
    (1,1), 
    (-1, 1), 
    (1, -1), 
    (-1, -1),
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)]

# function clousure to generate nextMoves function
def get_next_pointF(matrix):
    n = len(matrix)
    m = len(matrix[0])

    def nextMoves(point):

        all_moves = [(point[0] + move[0], point[1] +move[1]) for move in moves]

        range_filter = filter(lambda move: (0<=move[0]<n) and (0<=move[1]<m), all_moves)
        matrix_filter = filter(lambda move: matrix[move[0]][move[1]], range_filter)

        return set(matrix_filter)
    return nextMoves

# Complete the connectedCell function below.
def connectedCell(matrix):
    dfs = DFS()
    visited = {}
    new_points_f = get_next_pointF(matrix)
    max_result = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==1 and not visited.get((i, j), 0):
                dfs.search(start=(i,j), end=(-1,-1), moves=new_points_f, parent={})
                
                new_points = set(dfs.parent.keys())
                max_result = max(max_result, len(new_points))
                print('i,j', i, j)
                print('new points are ', *new_points)
                
                for p in new_points:
                    visited[p] = 1
    
    return max_result + (max_result==0)

if __name__=='__main__':

    with open('data/example3.data', 'r') as f:

        lines = f.read().rstrip().split('\n')
        matrix = [[int(num) for num in line.split()] for line in lines]

        new_points_f = get_next_pointF(matrix)
        print(*matrix, sep='\n')
        print('result:', connectedCell(matrix))
        