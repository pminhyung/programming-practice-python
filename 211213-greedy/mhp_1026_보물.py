"""
- 핵심 : 작은 수에 큰수를 곱
- list_a의 idx : list_b의 idx mapping
- list_b는 오름차순, list_a는 내림차순 정렬한 후 원본idx pair 생성 (k:v)
- alist2[b_idx] = alist[a_idx] : 원래 값을 blist 내 순서에 맞게 새로 위치
"""

import sys

inp = sys.stdin.readline
n = int(inp().rstrip())

alist = [(v, idx) for idx, v in enumerate( list(map(int, inp().rstrip().split())) )]
blist = [(v, idx) for idx, v in enumerate( list(map(int, inp().rstrip().split())) )]

idxa2b = {aid:bid for (_, aid),(_, bid) in zip(sorted(alist, reverse=True), sorted(blist))}
alist2 = [0]*n
for aid, bid in idxa2b.items():
    alist2[bid] = alist[aid]

print(sum([a*b for (a,_),(b,_) in zip(alist2, blist)]))
