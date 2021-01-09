"""
듣보잡 문제
author : donghak park
contact : donghark03@naver.com
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

answer = []
hear = []
saw = []

for _ in range(N):
    hear.append(input().rstrip())

for _ in range(M):
    saw.append(input().rstrip())

hear = set(hear)
saw = set(saw)

answer = list(hear.intersection(saw))

answer.sort()

print(len(answer))

for name in answer:
    print(name)
