import sys
inp = sys.stdin.readline
n, m = map(int, inp().rstrip().split())

visited = [False for _ in range(n+1)]
g = [False] + [[] for _ in range(n)]  # dummy
for _ in range(m):
    a, b = map(int, inp().rstrip().split())
    g[a].append(b)
    g[b].append(a)

def dfs(v):
    global visited
    stack = [v]
    while stack:
        curr = stack.pop()
        for after in g[curr]:
            if not visited[after] :
                stack.append(after)
                visited[after] = True

cnt = 0
for node in range(1, n+1):
    if not visited[node]:
        dfs(node)
        cnt+=1

print(cnt)