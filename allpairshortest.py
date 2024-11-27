def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]  
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

graph = [
    [0, 3, float('inf'), 7],
    [3, 0, 1, float('inf')],
    [float('inf'), 1, 0, 2],
    [7, float('inf'), 2, 0]
]

shortest_paths = floyd_warshall(graph)

print("Shortest path matrix:")
for row in shortest_paths:
    print(row)
