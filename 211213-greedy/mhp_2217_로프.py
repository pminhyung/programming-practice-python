"""
- rope 내림차순 정렬
- rope_idx 개를 사용할 때 최대중량 : rope * rope_idx
"""

import sys

inp = sys.stdin.readline
n = int(inp().rstrip())
ropes = sorted([int(inp().rstrip()) for _ in range(n)], reverse=True)

maxval = 0
for idx, r in enumerate(ropes, 1):
    maxval = max(r*idx, maxval)
print(maxval)