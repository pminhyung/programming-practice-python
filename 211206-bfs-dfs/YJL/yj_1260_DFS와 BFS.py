import sys
from collections import defaultdict
n, m, k = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


# print('n, m, k: ', n,m,k)
# print('graph:', graph)

# DFS - need_visit 스택과 visited 큐, 두 개의 자료 구조를 생성
def dfs(graph, v):
    visited, need_visit = list(), list()
    need_visit.append(v)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node], reverse=True))
    
    return visited

# BFS - need_visit 큐와 visited 큐, 두 개의 큐를 생성
def bfs(graph, k):
    visited, need_visit = list(), list()
    need_visit.append(k)
    
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node]))

    return visited


def printConfirm(result):
    for i in result:
        print(i, end=' ')

printConfirm(dfs(graph, k))
print()
printConfirm(bfs(graph, k))