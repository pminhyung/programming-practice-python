"""
(완료)

문제 세분화

1. A,B 현재 좌표 갱신
2. 해당 위치에서 A와 B의 충전량 합 max 구하기
3. 경로 이동하며 "1,2번"을 반복하여 충전량 누적합
"""


# A 혹은 B 우선시 각각 충전량 합 계산
def cal_result(charge1, charge2):

    ### charge len이 0일 때 index에러 발생... => for문 사용 (빈 리스트일 때도 에러X)
    # index, P = charge1[0]  # (i, P)
    # used = index
    # res = P

    used=None
    res=0

    for index, P in charge1:
        if len(charge1)!=0:
            used = index
            res = P
        else:
            return
        break

    for index, P in charge2:
        if len(charge2)!=0:
            if (index!=used) or used==None:
                res+=P
                break
    return res

# 충전
def charge(ax, ay, bx, by):
    a_charge, b_charge = [], []

    # 포함 충전소
    for i in range(len(AP)):
        ap = AP[i]
        x,y,C,P = ap[0], ap[1], ap[2], ap[3]
        if abs(ax-x)+abs(ay-y)<=C:
            a_charge.append((i, P))
        if abs(bx-x)+abs(by-y)<=C:
            b_charge.append((i, P))

        a_charge = sorted(a_charge, key = lambda x: x[1], reverse=True)
        b_charge = sorted(b_charge, key=lambda x: x[1], reverse=True)

        # a우선 혹은 b우선 시에 각각 충전량 합
        a_result, b_result = cal_result(a_charge, b_charge), cal_result(b_charge, a_charge)

    return max(a_result, b_result)


# input
T = int(input()) # T 테스트개수

for test_case in range(1, T+1):
    M, A = map(int, input().split()) # M 이동시간, A 충전소개수
    user_a = list(map(int, input().split())) # a 이동계획
    user_b = list(map(int, input().split())) # b 이동계획
    AP = [list(map(int,input().split())) for _ in range(A)] # AP정보들 (x,y,범위,처리량)

    # 초기상태 충전
    dx = [0, 0, 1, 0, -1] # x 좌표변화
    dy = [0, -1, 0, 1, 0] # y 좌표변화
    ax, ay = 1, 1
    bx, by = 10, 10
    tot = charge(ax, ay, bx, by) # tot 충전량 합(print)

    for i in range(M): # 이동시간 변화 -> 충전량 누적
        ax += dx[user_a[i]]
        ay += dy[user_a[i]]
        bx += dx[user_b[i]]
        by += dy[user_b[i]]
        tot+=charge(ax,ay,bx,by)

    print('#{} {}'.format(test_case, tot))