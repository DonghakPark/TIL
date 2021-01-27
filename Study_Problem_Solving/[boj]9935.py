"""
문자열 폭발 문제
author : donghak park
contact: donghark03@naver.com
"""
import sys
from collections import deque

input = sys.stdin.readline

S = list(input().rstrip())
bomb = list(input().rstrip())

temp = deque()

for s in S:
    temp.append(s)

    if len(temp) >= len(bomb):
        check = True

        for i in range(len(bomb)):
            if temp[len(temp)-len(bomb)+i] != bomb[i]:
                check = False

        if check == True:
            for _ in range(len(bomb)):
                temp.pop()
if temp:
    print(("").join(temp))
else:
    print("FRULA")