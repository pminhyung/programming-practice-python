# 연결 요소의 개수가 무엇인지 이해 못해서 풀이 보고 이해함
# https://my-coding-notes.tistory.com/211
##### 시간초과 -> 해결 같이 해보기

import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph)
# {1: [2, 5], 2: [1, 5], 5: [2, 1], 3: [4], 4: [3, 6], 6: [4]})

node_list = list()
for node in graph:
    node_list.append(node)

# print(node_list)
# [1, 2, 5, 3, 4, 6]

def dfs(graph, n):
    visited, need_visit = list(), list()
    need_visit.append(n)
    
    while need_visit:
        node = need_visit.pop(0)
        # IndexError: list index out of range
        # len(node_list) > 0 을 안해줬기 때문
        if len(node_list) > 0 and node == node_list[0]:
            node_list.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    
    return visited

count = 0
while len(node_list) > 0:
    dfs(graph, node_list[0])
    count += 1

print(count)

# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6

# 6 8
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 5 4
# 2 4
# 2 3