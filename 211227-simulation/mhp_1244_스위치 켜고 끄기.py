"""
- idea : 남 - 배수, 여 - 대칭 구현
- 출력 20개씩 조건 주의
- 스위치 바꾸기 : 1-arr[i]
- 함수 정의 시 list 객체 전체 수정 시에는 재할당이 아닌 새로운 변수에 할당 (에러 - Line10)
"""

# 남학생
def given_to_male(num):
    # arr  = [arr[i] if (i+1)%num else 1-arr[i] for i in range(n)]
    new_arr = [arr[i] if (i+1)%num else 1-arr[i] for i in range(n)]
    return new_arr

# 여학생
def given_to_female(num):
    idx = num-1
    start, end = (0, 0)
    for i in range(1, n//2):
        if 0<=idx-i<n and 0<=idx+i<n and arr[idx-i]==arr[idx+i]:
            # indice for slicing - [start:end]
            start = idx-i
            end = idx+i+1
        else:
            break

    if (start, end) == (0, 0):
        start = idx
        end = idx+1

    arr[start:end] = [1-arr[i] for i in range(start, end)]
    return arr

# main
import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
arr = list(map(int, inp().rstrip().split()))
num_iter = int(inp().rstrip())

for _ in range(num_iter):
    gender, num = map(int, inp().rstrip().split())
    if gender==1:
        arr = given_to_male(num)
    elif gender==2:
        arr = given_to_female(num)

# 출력
for i in range(0, n, 20):
    print(' '.join(map(str, arr[i:i+20])))

