# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def solution(a,b):
    """
    윤년은 2월이 29일까지
    인덱스니까 나머지 -1 해준만큼 리스트에서 요일 가줘야.
    :param a:
    :param b:
    :return:
    """
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b)%7-1]