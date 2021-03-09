"""
계단 수 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

N = int(input())
DP = [[[-1] * 11 for _ in range(101)] for _ in range(1 << 11)]
mod = 1000000000


def solution(f, b, x):
    if x < 0 or x > 9:
        return 0

    if b == N:
        if f == (1 << 10) - 1:
            return 1
        else:
            return 0

    if DP[f][b][x] != -1:
        return DP[f][b][x]
    DP[f][b][x] = 0
    if x == 0:
        DP[f][b][x] += solution(f | (1 << (x + 1)), b + 1, (x + 1))
        DP[f][b][x] %= mod
    elif x == 9:
        DP[f][b][x] += solution(f | (1 << (x - 1)), b + 1, (x - 1))
        DP[f][b][x] %= mod
    else:
        DP[f][b][x] += solution(f | (1 << (x + 1)), b + 1, (x + 1))
        DP[f][b][x] %= mod
        DP[f][b][x] += solution(f | (1 << (x - 1)), b + 1, (x - 1))
        DP[f][b][x] %= mod
    return DP[f][b][x]


answer = 0
for i in range(1, 10):
    answer += solution(1 << i, 1, i)
    answer %= mod
print(answer)
