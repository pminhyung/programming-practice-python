def solution(list_, commands):
    """ [a:b]가 마지막 b-1까지인 것 주의

    :param list_:
    :param commands:
    :return:
    """
    return [sorted(list_[i-1:j])[k-1] for i,j,k in commands]