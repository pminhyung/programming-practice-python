"""
candidate, final_result에서 메모리 초과 난듯하다...
"""
import sys
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline().strip())


def is_good(candidate, col):
    current_row=len(candidate)
    for queen_row in range(current_row):
        if current_row-queen_row==abs(candidate[queen_row]-col) or col == candidate[queen_row]:
            return False
    return True

def dfs(current_row, candidate):
    if current_row==n: # 마지막까지 도달 시, 한칸 더 내려오기 때문 (0~n-1 + 1)
        final_result.append(candidate[:])
        return

    for col in range(n):
        if is_good(candidate, col):
            candidate.append(col)
            dfs(current_row+1, candidate)
            candidate.pop()

final_result=[]
candidate=[]
dfs(0, candidate)
print(len(final_result))