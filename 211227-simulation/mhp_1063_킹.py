"""
- idea: obj 좌표 이동 구현
- stone 이동 불가인 경우 (stone 이동 시도 시) 고려 -> 원래 좌표로 설정 
"""
cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
id2col = {idx:col for idx, col in enumerate(cols)}
col2id = {col:idx for idx, col in enumerate(cols)}

# obj 좌표 index 변환 (row, col)
def get_row_col_idx(king, stone):
    col, row = king
    rowidx = int(row)-1
    colidx = col2id[col]

    col2, row2 = stone
    rowidx2 = int(row2)-1
    colidx2 = col2id[col2]
    return rowidx, colidx, rowidx2, colidx2

# obj 좌표 이동 (row, col)
def move_obj(comm, rowidx, colidx):
    r0, c0 = rowidx, colidx

    if comm == 'R':
        colidx+=1
    elif comm == 'L':
        colidx-=1
    elif comm == 'B':
        rowidx-=1
    elif comm == 'T':
        rowidx+=1
    elif comm == 'RT':
        rowidx+=1
        colidx+=1
    elif comm == 'LT':
        rowidx+=1
        colidx-=1
    elif comm == 'RB':
        rowidx-=1
        colidx+=1
    elif comm == 'LB':
        rowidx-=1
        colidx-=1

    if 0<=rowidx<8 and 0<=colidx<8:
        return rowidx, colidx
    else:
        return r0, c0

import sys
inp = sys.stdin.readline
king, stone, nmove = inp().rstrip().split()
krow, kcol, srow, scol = get_row_col_idx(king, stone)

for _ in range(int(nmove)):
    comm = inp().rstrip()
    kr0, kc0 = krow, kcol
    sr0, sc0 = srow, scol
    krow, kcol = move_obj(comm, kr0, kc0)
    moved_stone=False

    # king == stone
    if (krow, kcol) == (sr0, sc0):
        srow, scol = move_obj(comm, sr0, sc0)
        moved_stone = True
    # king == stone and stone 이동불가 시
    if moved_stone and (sr0, sc0) == (srow, scol):
        krow, kcol, srow, scol = kr0, kc0, sr0, sc0

res = id2col[kcol]+str(krow+1) + '\n' + id2col[scol]+str(srow+1)
print(res)