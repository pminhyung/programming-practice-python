import sys
n = int(sys.stdin.readline().strip())
stack = []
for _ in range(n):
    m = int(sys.stdin.readline().strip())
    if m==0:
        stack.pop()
        continue
    stack.append(m)
print(sum(stack))
