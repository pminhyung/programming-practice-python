import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
li = sys.stdin.readline().rstrip().split()
li.sort()


cs = combinations(li, L)
mo = ['a','e','i','o','u']

for c in cs:
	mocnt=0
	for letter in c:
		if letter in mo:
			mocnt+=1
	if mocnt>=1 and L-mocnt>=2:
		print(''.join(sorted(c)))