"""
단어 암기 문제
author : donghak park
contact: donghark03@naver.com
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = []
for _ in range(N):
    temp = list(input())
    S.append(temp)

alpha = [1] * 27

for _ in range(M):
    o, x = input().split()
    o = int(o)

    #잊는 경우
    if o == 1:
        alpha[ord(x) - 97] = 0

    #기억하는 경우
    else:
        alpha[ord(x) - 97] = 1

    answer = 0
    for element in S:
        flag = True
        for i in range(len(element)-1):
            if alpha[ord(element[i]) - 97] == 0:
                flag = False
                break
        if flag is True:
            answer += 1
    print(answer)