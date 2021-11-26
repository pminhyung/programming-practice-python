"""
원소당 차이(diff)를 구해서 모든 원소간 거리를 최소로 하는 문제와 같다
차이가 큰 원소 기준으로 구역을 나누는게 핵심

코너케이스: n<=k 일때 0을 출력하고 sys.exit()
"""
import sys
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

if n<=k:
    print(0)
    sys.exit()

arr.sort()
diff =[]
for i in range(len(arr)-1):
	diff.append(arr[i+1]-arr[i])

diff.sort(reverse=True)
for j in range(k-1):
	diff[j]=0
print(sum(diff))