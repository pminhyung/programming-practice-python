"""
- 최대회의개수 : 일찍 끝나는 회의를 (이른 종료 시간) 최대한 연달아 배치
- 회의를 종료시간, 시작시간 순으로 오름차순 정렬
"""

import sys
inp = sys.stdin.readline
n = int(inp().rstrip())

seminars = [list(map(int, inp().rstrip().split())) for _ in range(n)]
seminars = sorted(seminars, key = lambda x: (x[1], x[0])) # 종료시간, 시작시간 순서로 정렬

fin = 0
for seminar in seminars:
    # 시작 시
    if fin==0:
        cnt = 1
        fin = seminar[1]
        continue
    
    # 시작시간이 이전회의의 종료시간 이후여야
    if seminar[0] >= fin:
        fin = seminar[1]
        cnt+=1

print(cnt)