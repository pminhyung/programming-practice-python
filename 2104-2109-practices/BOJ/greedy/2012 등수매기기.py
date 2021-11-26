import sys
n = int(sys.stdin.readline().strip())
ranks=[]
for _ in range(n):
	ranks.append(int(sys.stdin.readline().strip()))

comp=0
for i, r in enumerate(sorted(ranks), 1):
	comp+=abs(i-r)
print(comp)