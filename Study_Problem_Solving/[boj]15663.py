"""
N과 M (9) 문제
author : donghak park
contact: donghark03@naver.com
"""
from itertools import permutations

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

answer = []
for candidate in list(permutations(num_list, M)):
    answer.append(candidate)

answer = sorted(list(set(answer)))

for ans in answer:
    for element in ans:
        print(element, end = " ")
    print()