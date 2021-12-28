"""
- idea : 앞뒤 비교 후 swap
"""
import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))
i = 0

# break 조건 : i==4 and arr == [1,2,3,4,5]
while i!=4 or arr != [1,2,3,4,5]:
    if i==4:
        i = 0
    if arr[i]>arr[i+1]:
        arr[i+1], arr[i] = arr[i], arr[i+1]
        print(' '.join(map(str, arr)))
    i+=1