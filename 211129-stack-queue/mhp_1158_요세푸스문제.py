import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
q = deque([i for i in range(1, n+1)])
res = []

while q:
	for idx in range(1, k+1):
		res.append(q.popleft()) if idx==k else q.append(q.popleft())

print('<'+', '.join(list(map(str, res)))+'>')