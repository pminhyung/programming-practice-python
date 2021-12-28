"""
- idea : 이진법, bin(n)에서 1의 개수가 K 초과 시, 가장 작은 자리 수의 1이 있는 값을 N에 추가

-- 이진법 사용 이유 : 같은 병 2개끼리 쌓을 수 있기 때문에, 2의 지수 단위로 표현 가능
-- 이 때 N을 이루는 2의 거듭제곱 숫자의 개수가 K개 이하여야 추가구매 불필요

-- bin(N)에서 1의 개수가 K 초과 시 추가구매 필요
-- 이 때 bin(N)에서 가장 작은 자리 수의 1을 더하면 K개 이하의 1로 표현 가능
"""
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
ans = 0

while str(bin(n)).count('1')>k:
    to_add = 2**int(str(bin(n))[::-1].index('1'))
    ans+=to_add
    n+=to_add
    
print(ans)
