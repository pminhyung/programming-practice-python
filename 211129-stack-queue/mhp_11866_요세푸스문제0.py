import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, n+1)])
res = []
while q:
	for i in range(1, m+1):
		if i==m:
			res.append(str(q.popleft()))
			break
		q.append(q.popleft())	
print('<'+', '.join(res)+'>')