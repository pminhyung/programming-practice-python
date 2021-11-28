import sys
from collections import deque
inp = sys.stdin.readline
n = int(inp().rstrip())

def run_command(comm, q):
    if comm[:len('push')] == 'push':
        _, x = comm.split()
        q.append(x)
    elif comm=='pop':
        print(q.popleft()) if q else print(-1)
    elif comm=='size':
        print(len(q))
    elif comm == 'empty':
        print(1) if not q else print(0)
    elif comm == 'front':
        print(q[0]) if q else print(-1)
    elif comm =='back':
        print(q[-1]) if q else print(-1)
    return q

q = deque()
for _ in range(n):
    command = inp().rstrip()
    q = run_command(command, q)
