"""
숫자 표현 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""


def solution(n):
    answer = 1
    num_list = [i for i in range(1, n + 1)]

    for i in range(n // 2 + 1):
        end = i
        while True:
            temp_sum = sum(num_list[i:end + 1])

            if temp_sum == n:
                answer += 1
                break
            elif temp_sum < n:
                end += 1
            else:
                break

    return answer
