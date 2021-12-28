
def get_pos(chess_loc):
    x = ord(chess_loc[0]) - ord('A')
    y = 8 - int(chess_loc[1])

    return x, y

king, stone, m = input().split()
kx, ky = get_pos(king)
sx, sy = get_pos(stone)

move_list = {
    'R': (1,0),
    'L': (-1, 0),
    'B' : (0,1),
    'T' : (0,-1),
    'RT' : (1, -1),
    'LT' : (-1, -1),
    'RB' : (1, 1),
    'LB' : (-1, 1)
}

for i in range(int(m)):
    location = input()
    dx, dy = move_list[location]
    king_nx = kx + dx
    king_ny = ky + dy
    
    if 0 <= king_nx < 8  and 0 <= king_ny < 8:
        if sx == king_nx and sy == king_ny:
            stone_nx, stone_ny = sx + dx, sy + dy
            if 0 <= stone_nx < 8 and 0 <= stone_ny < 8:
                sx, sy = stone_nx , stone_ny
                kx, ky = king_nx, king_ny
        else:
            kx, ky = king_nx, king_ny 


def get_cheese_pos(x_pos, y_pos):
    x = chr(x_pos + ord('A'))
    y = str(8 - y_pos)

    return x, y

kingArr = get_cheese_pos(kx, ky)
stonArr = get_cheese_pos(sx, sy)

for i in kingArr:
    print(i, end='')

print()

for j in stonArr:
    print(j, end='')