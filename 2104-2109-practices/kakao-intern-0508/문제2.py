places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
answer=[]

def get_nears(r,c):
    nears=[]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr<5 and 0<=nc<5:
            nears.append((i,nr,nc))
    return nears

def check(arr, r, c):
    nears = get_nears(r,c)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for d,r,c in nears: # 방향, row, column

        # 1) 주변에 P
        if arr[r][c]=='P':
            return False

        # 2) 빈자리 건너편 P
        if arr[r][c]=='O':
            nr = r+dr[d]
            nc = c+dc[d]
            if 0<=nr<5 and 0<=nc<5 and arr[nr][nc] =='P':
                return False

    # 3) 주변 2개 중 하나가 0일 때 대각선이 P여부
    for i in range(len(nears)-1):
        d1, r1, c1 = nears[i]
        _, r2, c2 = nears[i+1]
        if arr[r1][c1]=='O' or arr[r2][c2]=='O':
            if d1==0 or d1==2:
                if arr[r1][c2]=='P':
                    return False
            if d1==1 or d1==3:
                if arr[r2][c1]=='P':
                    return False

    return True


def test_case(arr):
    for i in range(5):
        for j in range(5):
            if arr[i][j]!='P':
                continue
            else:
                if not check(arr, i, j):
                    return False
    return True

for i in range(5):
    t = test_case(places[i])
    if t:
        answer.append(1)
    else:
        answer.append(0)

print(answer)