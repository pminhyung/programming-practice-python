def solution(phone_book):
    """
    sort 정렬 후 대상str.startswith(조건str) 으로 판단,
    zip(l1, l1[1:]) 일 때 l1[-2]에서 iter종료

    :param phone_book:
    :return:
    """
    phone_book = sorted(phone_book)
    print(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1, p2)
    #     if p2.startswith(p1):
    #         return False
    # return True

phone_book = ["119", "97674223", "1195524421"]
solution(phone_book)


def solution(phone_book):
    """
    각 번호를 hash의 key로 넣고,
    번호들을 iter하며 번호의 부분집합이 hash key에 존재하는지 (자기자신은 아님)을 확인

    """
    d = {k: 1 for k in phone_book}
    for p in phone_book:
        temp = ''
        for n in p:
            temp += n
            if (temp != p) and (temp in d):
                return False
    return True

