import sys
inp = sys.stdin.readline
n = int(inp().rstrip())

stack = []
for _ in range(n):
	num = int(inp().rstrip())
	stack.append(num) if num else stack.pop()
print(sum(stack))