"""
별 찍기 문제
author : donghak park
contact: donghark03@naver.com
"""
import math

answer = ["  *   ", " * *  ", "***** "]
def stars(space):
    length = len(answer)
    for i in range(length):
        answer.append(answer[i] + answer[i])
        answer[i] = ("   " * space + answer[i] + "   " * space)


N = int(input())
iterate = int(math.log(N//3, 2))

for i in range(iterate):
    stars(int(pow(2, i)))

for i in range(N):
    print(answer[i])