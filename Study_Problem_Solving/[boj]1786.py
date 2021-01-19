"""
찾기 문제
author : donghak park
contact: donghark03@naver.com
TODO : 다시 한번 풀어보기 -> KMP 알고리즘
"""


def make_pi():
    pi = [0 for i in range(0, len(P))]

    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]

        if (P[i] == P[j]):
            j += 1
            pi[i] = j
    return pi


def solution(pi):
    result = []
    count = 0

    j = 0
    for i in range(0, len(T)):

        while j > 0 and T[i] != P[j]:
            j = pi[j - 1]

        if T[i] == P[j]:
            if j == (len(P) - 1):
                result.append(i - len(P) + 2)
                count += 1
                j = pi[j]
            else:
                j += 1

    print(count)
    for element in result:
        print(element)


T = input()
P = input()
solution(make_pi())




