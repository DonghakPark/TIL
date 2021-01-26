"""
N과 M (2) 문제
author : donghak park
contact: donghark03@naver.com
"""
from itertools import combinations

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]

answer = list(combinations(arr, M))

for element in answer:
    for element2 in element:
        print(element2, end = " ")
    print()