"""
30배수 조건:
- 끝자리가 0
- 자리수 합이 3의 배수(sum3%3==0)
"""
import sys

def check_30(n):
    revnums = list(map(int, sorted(str(n), reverse=True)))
    if revnums[-1]:
        return -1
    if sum(revnums)%3:
        return -1
    return int(''.join(map(str, revnums)))

n = int(sys.stdin.readline().rstrip())
print(check_30(n))