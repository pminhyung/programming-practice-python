from itertools import combinations

"""경우의수 순열
"""
def solution(clothes):
    """
    곱으로 reduce 사용시에는 마지막인자(초기값)으로 1 넣어줄 것
    counter

    :param clothes:
    :return:
    """
    from collections import Counter
    from functools import reduce

    cnt = Counter([v for k, v in clothes])
    return reduce(lambda x,y: x*(y+1), cnt.values(), 1)-1

clothes= [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)

def solution(clothes):
    from functools import reduce
    d = {}
    for name, kind in clothes:
        if kind not in d:
            d[kind]=1
        else:
            d[kind]+=1
    ans = 1
    for value in d.values():

        ans*=(value+1)
    return ans-1
    #return reduce(lambda x,y: x*y, [v+1 for v in d.values()],1) -1