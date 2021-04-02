"""
쇠막대기 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
import sys
input = sys.stdin.readline

S = input()
answer = 0
still = 0
i = 0

while i < len(S):

    #레이저인 경우
    if S[i] == "(" and S[i+1] == ")":
        answer += still
        i += 2
    elif S[i] == "(":
        still += 1
        i += 1
    elif S[i] == ")":
        still -= 1
        answer += 1
        i += 1

print(answer)