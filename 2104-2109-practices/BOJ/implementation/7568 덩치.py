"""
간단하지만 처음이라 너무 어렵게 생각한 문제...

for문 2개로 각 샘플당 전체를 대상으로, 자신보다 확실하게 높은 샘플이 있을 때 본인 등수를 1씩 올리기만 하면 되었다
### 각자 나보다 확실히 큰 애가 몇명인가 만 구하면 된다!
(자신보다 확실하게 덩치가 큰 샘플이 몇개인가? n개 - 그러면 본인은 n+1로 등수 설정)

이러면 공동랭크를 고려한 뒤의 등수도 간단히 구할 수 있다
조정된 등수를 또 비교할 필요없다
"""
import sys
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline().strip())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
rank = [1]*n

for i in range(n):
    for j in range(n):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            rank[i]+=1
print(' '.join(map(str, rank)))