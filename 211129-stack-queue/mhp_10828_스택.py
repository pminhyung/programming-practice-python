"""
stack의 top == 나중에 들어온 것 (stack[-1])
"""

import sys
n = int(sys.stdin.readline().rstrip())

def perform(command, stack):
	if command[:len('push')] == 'push':
		_, num = command.split()
		stack.append(num) 
	elif command == 'pop':
		print(stack.pop()) if stack else print(-1)
	elif command == 'size':
		print(len(stack))
	elif command == 'empty':
		print(0) if stack else print(1)
	elif command == 'top':
		print(stack[-1]) if stack else print(-1)
	return stack
	
stack = []
for _ in range(n):
	command = sys.stdin.readline().rstrip()
	stack = perform(command, stack)
