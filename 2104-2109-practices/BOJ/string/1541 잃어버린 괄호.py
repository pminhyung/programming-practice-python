"""
한번 '-'를 만나면 그 뒤에 숫자는 모두 음수에 가산하는 것이 포인트..
"""

import sys
sys.setrecursionlimit(10**8)

arr = sys.stdin.readline().strip()
nums = arr.replace('+', ' ').replace('-', ' ').split()
op = [i for i in arr if not i.isdigit()]
is_minus=False
n = nums[0]
plus = [n]
minus= []
nums = nums[1:]

for i in range(len(nums)):
    if op[i]=='-':
        is_minus=True

    if nums[i].isdigit():
        if is_minus:
            minus.append(nums[i])
        else:
            plus.append(nums[i])

print(sum(map(int,plus))-sum(map(int,minus)))
