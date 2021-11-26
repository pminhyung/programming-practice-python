"""
- '(' append
- stack이 not empty이고 ')'일 때 pop
- stack이 empty인데 ')'일 때 NO return
- 최종 stack이 empty일 때 VPS
"""
import sys
inp = sys.stdin.readline
n = int(inp().rstrip())

stack = []

def isvps(pstring):
    if pstring[0] == ')':
        print('NO')
        return

    stack = []

    for p in pstring:
        if p=='(':
            stack.append(p)
        if not stack and p==')':
            print('NO')
            return
        if stack and p==')':
            stack.pop()
	
    print('NO') if stack else print('YES')

for _ in range(n):
	pstring = inp().rstrip()
	isvps(pstring)