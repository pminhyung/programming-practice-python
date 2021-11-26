"""
- 책의 현재위치가 0이고, 갖다놓을 위치가 각 좌표라는게 핵심 (가장 먼거리를 마지막에 한번 가고 끝냄)

- 먼 것부터 2개씩 끊어서, 먼것부터 우선 skip되게 하고 가까운 것을 왕복하게 해야함 (거리 최소 목표)

- 왕복이므로 기본적으로 거리x2 조심

- while문에서 추가로 pop할 때 for문 안에서 매번 if로 원소유무 검사해야 에러X

"""
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
pos, neg = list(), list()

for a in arr:
    if a > 0:
        heapq.heappush(pos, -a)
        continue
    if a < 0:
        heapq.heappush(neg, a)
        continue

large = -min(pos + neg)
res = 0
while pos:
    res += heapq.heappop(pos)
    for _ in range(m - 1):
        if pos:
            heapq.heappop(pos)

while neg:
    res += heapq.heappop(neg)
    for _ in range(m - 1):
        if neg:
            heapq.heappop(neg)

print(-(res*2 + large))