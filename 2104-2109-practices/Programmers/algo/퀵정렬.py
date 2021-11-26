# 재귀 - 원소개수 1일 때는 자신(list) 출력, 그렇지 않으면 qsort(left) + pivot + qsort(right) 반환
# pivot = list[0], left, right 리스트 활용
# O(nlogn) - 2로 나누면 logn 그리고 각 단계마다 n번의 비교
# pivot 가장 크거나 작을 때 n^2이 나온다


def qsort(li):
    if len(li)<=1:
        return li
    pivot = li[0]
    left, right = [], []
    for i in li[1:]: # pivot 제외하고 iter
        if pivot<=i:
            right.append(i)
        else:
            left.append(i)
    return qsort(left) + [pivot] + qsort(right)

def qsort(li): # list comprehension
    if len(li)<=1:
        return li
    pivot = li[0]
    left = [i for i in li[1:] if pivot>i]
    right = [i for i in li[1:] if pivot <= i]
    return qsort(left) + [pivot] + qsort(right)

def main():
    import random
    li = random.sample(range(100), 10)
    print(qsort(li))

main()