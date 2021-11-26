import sys
n = int(sys.stdin.readline().strip())

n = 1000-n
cnt=0
for coin in [500, 100, 50, 10, 5, 1]:
    cnt += n//coin
    n = n%coin
print(cnt)