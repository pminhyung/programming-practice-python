"""
- idea : set intersection 활용
"""
import sys
inp = sys.stdin.readline
n, m = map(int, inp().rstrip().split())

never_heard = [inp().rstrip() for _ in range(n)]
never_seen = [inp().rstrip() for _ in range(m)]
inter = sorted(list(set.intersection(set(never_heard), set(never_seen))))

print(f'{len(inter)}'+'\n'+'\n'.join(inter))