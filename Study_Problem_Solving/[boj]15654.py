"""
N과 M (5) 문제
author : donghak park
contact: donghark03@naver.com
"""
import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = list(permutations(arr, M))

for i in range(len(answer)):
    for j in range(M):
        print(answer[i][j], end = " ")
    print()