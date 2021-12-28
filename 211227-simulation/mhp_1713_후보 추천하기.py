"""
- idea : defaultdict + heapq 활용해서 오래된 학생 또는 적은표 학생 제외하며 업데이트

- heapq 사용 시 주의점
-- 일반 pop을 사용했을 때는 heappush를 사용해도
다음 heappop의 결과가 최솟값이 아닐 수 있음
-- heappop을 사용해야 heap의 root가 준비되기 때문
"""

"""
틀린 예외 케이스:
3
14
2 1 4 3 5 6 2 7 2 100 100 54 54 50
"""

import heapq, sys
from collections import defaultdict

def find_id(heap, reco_id):
    for idx, h in enumerate(heap):
        if h[2]==reco_id:
            return idx

inp =  sys.stdin.readline
nphoto = int(inp().rstrip())
ncand = int(inp().rstrip())
reco = list(map(int, inp().rstrip().split()))

heap = [] # [투표수, 게시 타이밍, 학생ID]
stat = defaultdict(lambda : 0) # {학생ID: 투표수}

t = 0
for i in range(ncand):
    reco_id = reco[i]

    # 사진 존재 : 학생 투표 수 수정
    if stat[reco_id]>0:
        idx = find_id(heap, reco_id)
        to_modify = list(heap.pop(idx))
        to_modify[0]+=1
        heap.append(tuple(to_modify))
        stat[to_modify[2]]+=1
        heapq.heapify(heap)
        continue

    # 사진 full : heapq에서 (오래된/적은 표) 학생 제외
    if len(heap)>=nphoto:
        pop_id = heapq.heappop(heap)[2]
        del stat[pop_id]

    # 사진에 학생 추가
    stat[reco_id]+=1
    to_add = (stat[reco_id], i, reco_id) # [투표수, 게시 타이밍, 학생ID]
    heapq.heappush(heap, to_add)

res = []
while heap:
    res.append(heapq.heappop(heap)[2])
print(' '.join(map(str, sorted(res))))    