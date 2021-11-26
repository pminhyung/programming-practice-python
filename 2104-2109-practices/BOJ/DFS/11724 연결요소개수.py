import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
g = [False] + [[] for _ in range(n)]
for _ in range(m):
	u, v = map(int, sys.stdin.readline().rstrip().split())
	g[u].append(v)
	g[v].append(u)

v = [False]*(n+1)

def dfs(node):
	global v
	stack = []
	stack.append(node)
	while stack:
		curr = stack.pop()
		for u in g[curr]:
			if not v[u]:
				stack.append(u)
				v[u] = True

cnt = 0
for i in range(1, n+1):
	if not v[i]:
		dfs(i)
		cnt+=1
print(cnt)