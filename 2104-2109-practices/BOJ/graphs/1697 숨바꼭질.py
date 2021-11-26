"""
bfs 활용
시작점 중복되어도 어차피 n-1, n+1, n*2 모두 1보다 크므로 pass된다

*** 런타임 인덱스에러: c*2가 배열길이를 넘었을 때 인덱스에러발생... => 범위 조건을 and 앞에 놓을것!!

"""

import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
g = [0]*100001
q=deque([n])

while q:
	c=q.popleft()
	if c==k:
		break
	for i in [c-1, c+1, c*2]:
		if (0<=i<=100000) and (g[i]==0):
			g[i]=g[c]+1
			q.append(i)
print(g[k])