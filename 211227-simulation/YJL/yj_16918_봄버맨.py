# 답은 맞게 나오는데 백준에선 틀렸습니다로 나옴...
# 그 이유는 상 하 좌 우 로 나타내서 인것 같음?
import sys
input = sys.stdin.readline 

R, C, N = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  

def findBomb():
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bombList.append((i,j))

    return bombList

def makeBomb():
    for i in range(R):
        for j in range(C):
            if board[i][j] != 'O':
                board[i][j] = 'O'

    return board

def explodeBomb():
    while bombList:
        x, y = bombList.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == 'O':
                    board[nx][ny] = '.'

N -= 1  # 1초 동안 아무것도 하지 않으므로
while N:
    bombList = []
    # 1. 폭탄이 어느 위치에 있는지 좌표값 구하기
    findBomb()
    # 2. 모든 칸에 폭탄 설치
    makeBomb()
    N -= 1
    if N == 0:
        break
    # 3. 폭탄 터지기
    # 3-1. 폭탄이 있는 상하좌우로 .으로 표시 폭탄도 .
    # 3-2. 폭탄이 안 터진 부분은 0으로 표시 계속해서 반복...
    explodeBomb()
    N -= 1

for i in range(R):
    for j in range(C):
        print(board[i][j], end='')
    print()

# --------------------------------------------------------
# https://li-fo.tistory.com/92
# 16918, 봄버맨
import sys
from collections import deque


def loc_bombs():    # 폭탄 위치 찾아 bombs deque에 저장
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bombs.append((i, j))


def make_bombs():   # 모든 자리에 폭탄 설치
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 'O'


def explode():      # bombs deque에 들어있는 좌표로 폭탄 터트림
    while bombs:
        r, c = bombs.popleft()
        board[r][c] = '.'
        if 0 <= r - 1:
            board[r - 1][c] = '.'
        if r + 1 < R:
            board[r + 1][c] = '.'
        if 0 <= c - 1:
            board[r][c - 1] = '.'
        if c + 1 < C:
            board[r][c + 1] = '.'


R, C, N = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

N -= 1  # 1초 동안 아무것도 하지 않는다
while N:
    bombs = deque()
    loc_bombs()
    make_bombs()
    N -= 1
    if N == 0:
        break
    explode()
    N -= 1

for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end='')
    print()