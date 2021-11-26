from collections import Counter
def solution(s):
    d = Counter(s.lower())
    if ('p' in d) and ('y' in d):
        if d['p'] == d['y']:
            return True
    return False

def numPY(s):
    """
    list.count(원소) ... 예외처리도 필요없다
    :param s: 
    :return: 
    """
    return s.lower().count('p') == s.lower().count('y')