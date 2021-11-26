def sumMatrix(A,B):
    """
    임의로 영행렬 만들지 말 것 (수정이 이상하게 일어남, numpy array와 다름)
    :param A:
    :param B:
    :return:
    """
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

def solution(A, B):
    return [[l1+l2 for l1, l2 in zip(li1, li2)] for li1, li2 in zip(A,B)]
