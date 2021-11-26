"""
heappush, heappop을 사용하면 최솟값을 자동으로 pop할 수 있다 (시간복잡도 줄이는데 유용)
"""
import sys
import heapq

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    d, c = map(int, sys.stdin.readline().split())
    arr.append((d, c))

arr = sorted(arr, key=lambda x: x[0])
ramens = []

for i in arr:
    heapq.heappush(ramens, i[1])
    if len(ramens) <= i[0]:
        continue
    else:
        heapq.heappop(ramens)

print(sum(ramens))