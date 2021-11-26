"""
2차원 배열 형성
행: 물건개수, 열: 제한무게
값: 해당 물건(행)까지 사용가능할 때, 제한무게 당(열) 최대 가치

line 20: 물건 무게보다 제한무게가 낮을 때는 이전 행의 동일 열 값들을 그대로 가져온다(최대값 그대로 사용)
line 22: 제한무게가 높을 때는 이전 물건들만 사용할 때 최대가치, 현재 물건 함께 담을 때 최대가치 중 최댓값을 넣어준다

"""
import sys

n, k = map(int, sys.stdin.readline().split())

arr = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, sys.stdin.readline().split())
    for j in range(1, k+1):
        if w > j:
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-w]+v) #

print(arr[n][k])