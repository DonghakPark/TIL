"""
2021 상반기 코딩테스트 대비 연습 문제 풀이
Author : DongHak Park
Contact: donghark03@naver.com
"""

def solution(n):
    answer = 0
    mod = 1000000007
    dp_table = [0] * (n + 1)
    dp_table[1] = 1
    dp_table[2] = 2

    for index in range(3, n + 1):
        dp_table[index] = (dp_table[index - 1] + dp_table[index - 2]) % mod

    answer = dp_table[n]

    return answer
