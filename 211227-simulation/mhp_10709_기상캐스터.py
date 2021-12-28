"""
- idea : 구름 발견 전 cache -1 저장 / 구름 발견 후 cache 0 저장, 이후 . 일때 1씩 증가
"""
import sys
inp = sys.stdin.readline
h, w = map(int, inp().rstrip().split())
arr = [inp().rstrip() for _ in range(h)]
res = [[] for _ in range(h)]

for i in range(h):
    cache = -1
    for j in range(w):
        if arr[i][j] == 'c':
            cache = 0
            res[i].append(cache)
        elif cache==-1 and arr[i][j] == '.':
            res[i].append(cache)
        elif cache!=-1 and arr[i][j] == '.':
            cache+=1
            res[i].append(cache)

for i in range(h):
    print(' '.join(map(str, res[i])))