"""
팩토리얼 0의 개수 문제
author : donghak park
contact : donghark03@naver.com
"""
import math

N = int(input())
number = str(math.factorial(N))

answer = 0

for i in range(len(number)-1, -1, -1):
    if number[i] == "0":
        answer += 1
    else:
        break

print(answer)