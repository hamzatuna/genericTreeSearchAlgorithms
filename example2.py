from collections import defaultdict

from generics import BFS

def solve(graph, start, num_nodes):
    nextF = lambda node: graph[node-1]
    results = [-1 for _ in range(num_nodes)]
    bfs = BFS(start, -1)
    bfs.search(nextF)
    for node in range(1, num_nodes+1):
        if node == start:
            continue
        
        cost = bfs.cost.get(node, None)
        if cost:
            results[node-1] = (cost)*6
    results.pop(start-1)
    return results

def main():
    with open('example2.data', 'r') as f:
        lines = f.read().rstrip().split('\n')
        
        
        num_nodes, edges = list(map(int, lines[0].split()))
        graph = [[] for _ in range(num_nodes)]

        start = int(lines[-1])

        for line in lines[1:-1] :
            node1, node2 = list(map(int, line.split()))
            graph[node1-1].append(node2)
            graph[node2-1].append(node1)
        
    print(*solve(graph, start, num_nodes))


if __name__=='__main__':
    main()