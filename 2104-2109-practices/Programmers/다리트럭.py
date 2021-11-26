#while len(대기)!=0

#매초 (다리트럭)과 (대기 첫번째 트럭) 합이 10 이하면 (다리)에 (대기 첫번째 트럭) 추가 (len(다리)==0 제외)ㅇ


#다리에 추가된지 (다리길이)초마다 해당트럭 다리 -> 지남
#- 매초 다리트럭에 대해, for 트럭 in 다리: if 트럭 not in d: d[트럭]=0 else: d[트럭]+=1
#- if d[다리맨앞트럭]==다리길이: d[다리맨앞트럭]=0 else: pass

from itertools import cycle, permutations
print(list(permutations([1,2,3], 2)))
print('123'.split())