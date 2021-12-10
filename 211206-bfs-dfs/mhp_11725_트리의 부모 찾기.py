"""
- 단순하게 1부터 dfs 실행하면 tree 순회 가능
- dfs에서 연결노드가 부모인지 check
"""

import sys

def dfs():
    stack = [1]
    while stack:
        curr = stack.pop()
        for son in g[curr]:
            if parents[curr]==son: # 부모는 pass
                continue
            parents[son] = curr
            stack.append(son)

inp = sys.stdin.readline
n = int(inp().rstrip())

# dummy (1<=n)
g = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

# tree
for _ in range(n-1):
    a, b = map(int, inp().rstrip().split())
    g[a].append(b)
    g[b].append(a)

# parents 저장 (dfs)
dfs()

print('\n'.join(map(str, parents[2:])))