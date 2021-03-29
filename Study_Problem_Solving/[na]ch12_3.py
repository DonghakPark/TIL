"""
문자열 압축 문제
author : donghak park
contact : donghark03@naver.com
"""


def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1

            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev

        answer = min(answer, len(compressed))

    return answer


if __name__ == "__main__":
    t1 = "aabbaccc"
    t2 = "ababcdcdababcdcd"
    t3 = "abcabcdede"
    t4 = "abcabcabcabcdededededede"
    t5 = "xababcdcdababcdcd"

    print(solution(t1))
    print(solution(t2))
    print(solution(t3))
    print(solution(t4))
    print(solution(t5))
