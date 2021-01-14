"""
패션왕 신해빈 문제
author : donghak park
contact: donghark03@naver.com
"""

T = int(input())

for test_case in range(T):
    N = int(input())
    cloth = {}

    for _ in range(N):
        name, what = input().split()

        if what in cloth.keys():
            cloth[what].append(name)
        else:
            cloth[what] = [name,""]
    answer = 1
    for key in cloth.keys():
        answer *= len(cloth[key])

    print(answer - 1 )