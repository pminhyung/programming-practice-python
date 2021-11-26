# 문제잘읽기 - 터뜨린 인형개수 return
# move 수행 후 break 필요!
import numpy as np
def solution(board = [[0,0,0,0,0],
                      [0,0,1,0,3],
                      [0,2,5,0,1],
                      [4,2,4,4,2],
                      [3,5,1,3,1]], moves = [1,5,3,5,1,2,1,4]):
    answers = []
    last = None
    cnt = 0
    for n_col in moves:
        if board[-1][n_col - 1] == 0:
            continue
        for n_row in range(len(board)):
            value = board[n_row][n_col - 1]
            if value == 0:
                continue

            if (len(answers)>0) and (value == answers[-1]):
                answers.pop()
                cnt+=2
            else:
                answers.append(value)

            board[n_row][n_col - 1] = 0
            last = value
            break
    return cnt

[[0,0,0,0,0],
 [0,0,1,0,3],
 [0,2,5,0,1],
 [4,2,4,4,2],
 [3,5,1,3,1]]