def solution(arr):
    """
    마지막 숫자를 prev에 넣어 다음 숫자와 대조
    :param arr:
    :return:
    """
    nums = []
    prev = None
    for i in arr:
        if i!=prev:
            nums.append(i)
            prev = i
    return nums