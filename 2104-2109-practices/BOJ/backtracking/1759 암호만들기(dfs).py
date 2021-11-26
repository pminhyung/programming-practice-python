"""
combination
"""

import sys

L, C = map(int, sys.stdin.readline().split())
li = sys.stdin.readline().rstrip().split()
li.sort()

import copy
temp = []
result = []
visited = []

def combination(arr, length, index):
    if len(temp)==length:
        result.append(copy.deepcopy(temp))
        return
    for i in range(index, len(arr)):
        if i in visited:
            continue
        temp.append(arr[i])
        visited.append(i)
        combination(arr, length, i+1)
        temp.pop()
        visited.pop()

combination(li, L, 0)
mo = ['a','e','i','o','u']

for c in result:
    mocnt=0
    for letter in c:
        if letter in mo:
            mocnt+=1
    if mocnt>=1 and L-mocnt>=2:
        print(''.join(sorted(c)))
