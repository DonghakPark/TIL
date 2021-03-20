"""
그룹 단어 체커 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
import sys
input = sys.stdin.readline

N = int(input())
answer = [True] * N
for i in range(N):
    S = input()
    check = []
    for j in range(len(S)):
        if j == 0:
            check.append(S[j])
        elif S[j] not in check and S[j] != S[j-1]:
            check.append(S[j])
        elif S[j] in check and S[j] == S[j-1]:
            continue
        else:
            answer[i] = False
            break
print(answer.count(True))
