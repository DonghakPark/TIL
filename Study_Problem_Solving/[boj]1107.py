"""
리모컨 문제
author : donghak park
contact : donghark03@naver.com
"""
import sys
input = sys.stdin.readline

def possible_num(x):
    x = list(str(x))
    for element in x:
        if element in err:
            return False
    return True

N = int(input())
M = int(input())
err = list(input().strip())

answer = abs(N - 100)

for temp in range(1000001):
    if possible_num(temp) is True:
        answer = min(answer, len(str(temp)) + abs(N-temp))
print(answer)