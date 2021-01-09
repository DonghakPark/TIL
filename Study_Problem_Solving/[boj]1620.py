"""
나는야 포켓몬 마스터 이다솜
author : donghak park
contact : donghark03@naver.com
"""

N, M = map(int, input().split())
name = {}
number = {}
start = 1

for _ in range(N):
    n = input().strip()
    name[n] = start
    number[start] = n
    start += 1

for _ in range(M):
    problem = input().strip()
    if problem.isnumeric():
        print(number[int(problem)])
    else:
        print(name[problem])
