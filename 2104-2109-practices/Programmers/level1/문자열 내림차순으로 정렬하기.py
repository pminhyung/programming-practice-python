def solution(strings):
    so = ''.join(sorted([s for s in strings if s.islower()], reverse=True))
    dae = ''.join(sorted(''.join([s for s in strings if s.isupper()]), reverse=True))
    return so+dae

def solution(strings):
    """
    대문자가 소문자보다 앞선다 (오름차순 시 앞에 위치)
    :param strings:
    :return:
    """
    return ''.join(sorted(strings, reverse=True))