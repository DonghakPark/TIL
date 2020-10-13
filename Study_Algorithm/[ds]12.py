# 시험 감독 문제
import math

N = int(input())

A = (list(map(int, input().split())))
B,C = map(int, input().split())

total = 0

for i in range(N):
    if A[i] <= B:
        total += 1
    else:
        total += math.ceil((A[i] - B)/C) + 1

print(total)