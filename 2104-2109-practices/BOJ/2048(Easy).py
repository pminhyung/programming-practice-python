size = int(input())
arr = [[] for _ in range(size)]
for i in range(size):
    row = list(map(int, input().split()))
    arr[i].extend(row)
