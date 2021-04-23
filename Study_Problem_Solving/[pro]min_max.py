"""
최대 최소 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""


def solution(s):
    answer = ''
    new_list = list(map(int, s.split()))
    answer = str(min(new_list)) + " " + str(max(new_list))
    return answer
