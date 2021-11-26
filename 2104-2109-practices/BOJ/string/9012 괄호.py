"""
스택활용
"""
import sys
sys.setrecursionlimit(10**8)

T = int(sys.stdin.readline().strip())

for _ in range(T):
    arr = sys.stdin.readline().strip()
    stack = []
    is_no = False
    for a in arr:
        if a=='(':
            stack.append(1)
            continue

        if len(stack)!=0:
            stack.pop()
            continue

        is_no=True
        break

    if is_no:
        print('NO')
        continue

    if len(stack)==0:
        print('YES')
        continue

    print('NO')






