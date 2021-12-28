# 시뮬레이션 알고리즘이란?
# 각 조건에 맞는 상황을 구현하는 문제
## 지도나 배열에서 이동하면서 탐험하는 문제
# 별도의 알고리즘 없이 풀 수 있으나, 구현력이 중요
# 매 시험마다 1문제 이상 출제

# -----------------------------
# 남학생은 1로, 여학생은 2
# 런타임 에러 (IndexError) -> 1부터 연속적으로 번호가 붙어있는 스위치
import sys
read = sys.stdin.readline
n = int(read())
switch_arr = [-1] + list(map(int, read().rstrip().split()))
gender = int(read())

def onandoff(num):
    if switch_arr[num] == 0:
        switch_arr[num] = 1
    else:
        switch_arr[num] = 0
    return

for _ in range(gender):
    g, s = map(int, read().rstrip().split())

    if g == 1:
        if s == 8:
            onandoff(s)
        else:
            for m in range(1, len(switch_arr) // s):
                # print('m', m)
                # m -> 1, 2
                onandoff((s * m))
        
    if g == 2:
        onandoff(s)
        if s != 1 and s != n:
            for w in range(1, len(switch_arr) // s):
                # print('w', w)
                # w -> 1, 2
                if switch_arr[(s + w)] == switch_arr[(s - w)]:
                    onandoff((s + w))
                    onandoff((s - w))
        

for i in range(1, n+1):
    print(switch_arr[i], end = " ")


# 기존 코드 "틀렸습니다" 계속 나옴
# 이유 모르겠음...
# https://codinghani.tistory.com/30


def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, N+1, num):
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N//2):
            if num + k > N or num - k < 1 : break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break
                
for i in range(1, N+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()