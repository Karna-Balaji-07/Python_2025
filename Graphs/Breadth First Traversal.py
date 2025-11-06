# Breadth first traversal in an undirected graph

from collections import deque
def BFS(adj):
    v = len(adj)
    visited = [False] * v
    result = []

    source = 0
    q = deque()
    visited[source] = True
    q.append(source)

    while q:
        curr  = q.popleft()
        result.append(curr)
        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

    return result

