def solution(n):
    """
    float - int(버림) 차이 존재 시 정수제곱근 X
    :param n:
    :return:
    """
    return (n**.5+1)**2 if (n**.5)-int((n**.5))==0 else -1