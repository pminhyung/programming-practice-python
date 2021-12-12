"""
가장 큰 동전부터 count
"""

import sys
inp = sys.stdin.readline
n, k = map(int,(inp().rstrip().split()))
coins = sorted([int(inp().rstrip()) for _ in range(n)], reverse=True)

def get_mincnt(k, coins):
    cnt = 0
    for coin in coins:
        mod, rem = divmod(k, coin)
        cnt+=mod
        k=rem
    return cnt

print(get_mincnt(k, coins))

