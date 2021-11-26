"""
i, j 순회마다 두문자열에 각각 한자씩 더했을 때 개수를 따져야하므로 arr[i-1][j-1]보다 1을 더해줘야한다
arr[i][j]에서 s1과 s2의 추가된 글자가 다를 때는 max(arr[i - 1][j], arr[i][j - 1]) 를 통해 각각 이전 것을 비교해서 큰 것으로 넣어준다
"""
import sys

s1 = ' ' + sys.stdin.readline().strip()
s2 = ' ' + sys.stdin.readline().strip()
n = len(s1)
m = len(s2)

arr = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            arr[i][j] = 0
            continue
        if s1[i] == s2[j]:
            arr[i][j] = arr[i - 1][j - 1] + 1
            continue
        arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

print(arr)
print(arr[n - 1][m - 1])