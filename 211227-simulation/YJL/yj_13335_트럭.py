# n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중
# 계속해서 runtime error남 -> 함수로 빼니깐 에러 안남
# https://chelseashin.tistory.com/98

import sys
input = sys.stdin.readline 

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

# bridge = [0] * W
# count = 0

# while trucks:
#     count += 1
#     bridge.pop(0)
#     if bridge:
#         if sum(bridge) + trucks[0] <= L:
#             bridge.append(trucks.pop(0))
#         else:
#             bridge.append(0)

# # trucks에 요소가 없어지는 순간 반복문 끝나므로 
# # 다리의 길이만큼 count에 추가
# print(count + W)

def solve():
    bridge = [0] * W
    count = 0
    while trucks:
        bridge.pop(0)		# 다리에서 단위 길이만큼 이동
        x = trucks[0]			# trucks의 첫번째 트럭 무게
        if len(bridge) < W and sum(bridge) + x <= L:	# 중요!
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)	# pop하지 못했다면 단위 길이만큼 이동 표현
        count += 1
    # trucks에 요소가 없어지는 순간 반복문 끝나므로 다리의 길이만큼 time에 추가
    return count + W

print(solve())