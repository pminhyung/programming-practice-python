"""
- 소요시간 별 오름차순 정렬이 핵심
"""
import sys
inp = sys.stdin.readline

n = int(inp().rstrip())
pn = map(int, inp().rstrip().split())

pn = sorted(pn)
spend = [sum(pn[:i+1]) for i in range(n)]
print(sum(spend))