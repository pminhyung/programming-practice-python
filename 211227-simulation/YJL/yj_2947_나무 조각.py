# 버블정렬? 같은 문제
import sys
treeList = list(map(int, sys.stdin.readline().rstrip().split()))

while True:
  for i in range(len(treeList) - 1):
    if treeList[i] > treeList[i + 1]:
      temp = treeList[i]
      treeList[i] = treeList[i + 1]
      treeList[i + 1] = temp
      print(' '.join(map(str, treeList)))

  if treeList == [1, 2, 3, 4, 5]: break