"""
작업 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())

dp_table = [0] * (N + 1)
degree = [0] * (N + 1)
dependency = defaultdict(list)
work_time = [0] * (N + 1)

for i in range(1, N + 1):
    S = list(map(int, input().split()))

    work_time[i] = S[0]
    degree[i] = S[1]
    for element in S[2:]:
        dependency[element].append(i)

Q = deque()

for i in range(1, len(degree)):
    if degree[i] == 0:
        Q.append(i)
        dp_table[i] = work_time[i]

while Q:
    now = Q.popleft()
    for element in dependency[now]:
        degree[element] -= 1
        dp_table[element] = max(dp_table[element], dp_table[now] + work_time[element])
        if degree[element] == 0:
            Q.append(element)

print(max(dp_table))
