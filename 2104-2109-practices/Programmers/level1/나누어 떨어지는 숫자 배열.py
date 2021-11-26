def solution(arr, divisor):
    li = sorted([a for a in arr if not a%divisor])
    if len(li)==0:
        return [-1]
    return li

def solution(arr, divisor):
    """
    앞에 값이 0(False)이면 뒤에 값을 반환하도록 [-1]
    :param arr:
    :param divisor:
    :return:
    """
    return sorted([n for n in arr if n%divisor == 0]) or [-1]