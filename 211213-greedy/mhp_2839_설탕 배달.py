"""
3kg, 5kg -> n kg (최대한 적은 봉지)

- 5kg의 몫만큼 다 사용하지 않더라도 나머지를 3kg로 채울 수 있는 case가 존재!
- 5kg 개수를 0부터 n//5까지 늘려가며 결과 append
- 최솟값 또는 -1 반환
"""

import sys

def get_mincnt(n):
    ans = []
    for mod5 in range(n//5+1):
        rem5 = n-(mod5*5)
        mod53, rem53 = divmod(rem5, 3)
        if rem53%3==0:
            ans.append(mod5+mod53)

    return min(ans) if ans else -1

n = int(sys.stdin.readline().rstrip())
print(get_mincnt(n))