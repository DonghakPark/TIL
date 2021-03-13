"""
외판원 순회 문제
Author : DongHak Park
Contact: donghark03@naver.com
TODO : 다시 풀어 볼 것
"""
import sys
input = sys.stdin.readline
INF = sys.maxsize


def find_path(last, visited):
    if visited == (1<<N) - 1:
        return travel_map[last][0] or INF

    if dp_table[last][visited] is not None:
        return dp_table[last][visited]

    temp = INF
    for city in range(N):
        if visited & (1 << city) == 0 and travel_map[last][city] != 0:
            temp = min(temp,
                       find_path(city, visited | (1 << city)) + travel_map[last][city])
    dp_table[last][visited] = temp
    return temp

N = int(input())
travel_map = [list(map(int, input().split())) for _ in range(N)]
dp_table = [[None] * (1 << N) for _ in range(N)]

print(find_path(0, 1<<0))
