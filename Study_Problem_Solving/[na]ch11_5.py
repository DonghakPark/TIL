"""
볼링공 고르기 문제
author : donghak park
contact : donghark03@naver.com
"""
from itertools import combinations

N, M = map(int, input().split())
ball = list(map(int, input().split()))

result = list(combinations(ball, 2))
answer = 0

for element in result:
    if element[0] == element[1]:
        continue
    else:
        answer += 1
print(answer)

"""
책 풀이
"""
# n,m = map(int, input().split())
# data = list(map(int, input().split()))
#
# array = [0] * 11
#
# for x in data:
#     array[x] += 1
#
# result = 0
# for i in range(1, m+1):
#     n -= array[i]
#     result += array[i] * n
#
# print(result)