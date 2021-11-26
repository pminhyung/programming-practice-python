# O(logn)
def binary_search(data, search):
    print(data)
    # 개수가 하나일 때 - 일치: True, 불일치: False
    if len(data)==0 and search == data[0]:
        return True
    if len(data)==0 and search!=data[0]:
        return False

    # 인덱스 숫자: 5개면 2(3번째), 4개면 3(2번째)
    mid = len(data)//2

    # 중간 원소와 일치 : True
    if data[mid]==search:
        return True
    # 중간원소보다 클 때: 중간원소 이후 반환
    if data[mid]<search:
        return binary_search(data[mid+1:],search)
    # 중간원소보다 작거나 같을 때: 중간원소까지 반환
    else:
        return binary_search(data[:mid+1], search)


def main():
    li = [71, 40, 1, 98, 57, 5, 27, 97, 26, 3]
    #import random
    #li = random.sample(range(100), 10)
    #print(li)
    return binary_search(sorted(li), 97)
print(main())