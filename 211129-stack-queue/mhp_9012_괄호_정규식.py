# 정규식 풀이
import sys, re
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    prev = sys.stdin.readline().rstrip()
    after = prev
    while True:
        after = re.sub('\(\)', '', prev)
        if prev==after:
            break
        prev = after
    print('YES') if after == '' else print('NO')