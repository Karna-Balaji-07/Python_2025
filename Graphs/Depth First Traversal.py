# Depth first traversal / DFS of undirected graphs

def DFSrec(adj,visited, node, result):
    visited[node] = True
    result.append(node)

    for i in adj[node]:
        if not visited[i]:
            DFSrec(adj, visited,i, result)

def dfs(adj):
    visited = [False] * len(adj)
    result = []
    DFSrec(adj, visited, 0, result)
    return result