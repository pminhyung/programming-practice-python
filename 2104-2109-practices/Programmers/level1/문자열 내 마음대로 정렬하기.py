def solution(strings, n):
    """
    처음에 sort하고 이후에 n번째 글자로 sort한다
    :param strings:
    :param n:
    :return:
    """
    return sorted(sorted(strings), key = lambda x: x[n])


def solution(strings, n):
    """
    n번째 글자를 첫번째로 가져와 sort 후 다시 원래자리에 놓는다
    :param strings:
    :param n:
    :return:
    """
    sort_str = sorted([s[n] + s[:n] + s[n + 1:] for s in strings])
    return [s[1:n + 1] + s[0] + s[n + 1:] for s in sort_str]
