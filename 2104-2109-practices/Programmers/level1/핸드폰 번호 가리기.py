def solution(phone_number):
    return ''.join([str(phone_number[i]) if i>len(phone_number)-5 else '*' for i in range(len(phone_number))])

def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]