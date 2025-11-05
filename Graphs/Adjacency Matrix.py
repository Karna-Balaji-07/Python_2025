# Adjacency matrix of undirected graph unweighted graph
def create_graph(v,edges):
    matrix = [[0] * v for i in range(v)]
    for i in edges:
        v= i[0]
        u = i[1]
        matrix[v][u] = 1
        matrix[u][v] = 1
    return matrix

#Adjacency matrix for directed graph
def create_graph1(v, edges):
    matrix = [[0]*v for i in range(v)]
    for i in edges:
        v = i[0]
        u = i[1]
        matrix[v][u] = 1
    return matrix


