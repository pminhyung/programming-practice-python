import sys
n = int(sys.stdin.readline())

cnt = 0
remains = 1000-n
for coin in [500, 100, 50, 10, 5, 1]:
    if remains==0:
        break
    mod, remains = divmod(remains, coin)
    cnt+=mod
print(cnt)