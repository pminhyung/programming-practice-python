import sys
from collections import defaultdict

computer = int(sys.stdin.readline())
contact = int(sys.stdin.readline())

graph = defaultdict(list)

for i in range(contact):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
# print(graph)

def bfs(graph, f):
    visited, need_visit = list(), list()
    need_visit.append(f)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node]))

    return visited

print(len(bfs(graph, 1))-1)


