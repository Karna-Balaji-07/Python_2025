# Adjacency list for undirected graph
def solution1(v, edges):
    lists = [[] for i in range(v)]
    for i in edges:
        v = i[0]
        u = i[1]
        lists[v].append(u)
        lists[u].append(v)
    return lists

#Adjacency list for directed graph
def solution2(v, edges):
    lists = [[]for i in range(v)]
    for i in edges:
        v = i[1]
        u = i[0]
        lists[u].append(v)
    return lists
