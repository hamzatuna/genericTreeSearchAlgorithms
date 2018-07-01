from generics import  BFS, DFS, AStar
# hacker rank knightL on chessboard solution

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


def main():
    print(get_dis_matrix(5))


if __name__ == '__main__':
    main()