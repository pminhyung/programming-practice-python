def solution(s):
    if s[0]=='-':
        return 0-int(s[1:])
    return int(s)

def strToInt(str):
    """
    음수여도 int 바꾸면 음수로 변환
    :param str: 
    :return: 
    """
    a = int(str)
    return a