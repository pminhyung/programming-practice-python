import sys

inp = sys.stdin.readline
n = int(inp().rstrip())

res = []
stack = []
curr = 1 # stack 추가 시작 숫자
is_no = False

for _ in range(n):

	num = int(inp().rstrip())
	
	while curr<=num:
		stack.append(curr)
		res.append('+')
		curr+=1
		
	if num==stack[-1]:
		stack.pop()
		res.append('-')
	else:
		is_no = True
		break
		
print('NO') if is_no else print('\n'.join(res))