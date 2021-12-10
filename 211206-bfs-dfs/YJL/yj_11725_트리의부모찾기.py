# https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-11725%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Tree-dfs-bfs
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if parent[i] == 0:
                parent[i] = node
                q.append(i)
                # print(q)

    return parent

bfs()

for i in parent[2:]:
    print(i)