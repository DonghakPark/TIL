"""
영어 끝말잇기 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""


def solution(n, words):
    answer = [0, 0]

    person_num = 0
    count = 1
    used = []
    while words:
        now = words.pop(0)

        if now in used:
            answer = [person_num + 1, count]
            return answer
        elif used:
            if used[-1][-1] != now[0]:
                answer = [person_num + 1, count]
                return answer

        used.append(now)
        person_num = (person_num + 1) % n
        if person_num == 0:
            count += 1

    return answer

