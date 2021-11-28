"""
- range(1, n+1)인 것 확인
"""
import sys
from collections import deque

inp = sys.stdin.readline
n = int(inp().rstrip())
q = deque([i for i in range(1, n+1)])

cnt = 0
while len(q)>1:
	if not cnt%2:
		q.popleft()
	else:
		q.append(q.popleft())
	cnt+=1
	
print(q.popleft())