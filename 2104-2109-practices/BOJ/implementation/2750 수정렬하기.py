"""
선택정렬 사용
sorted도 사용가능
"""
import sys
n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]

for i in range(n):
    prev = i
    for j in range(i+1, n):
        if arr[i]>arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for i in range(n):
    print(arr[i])
