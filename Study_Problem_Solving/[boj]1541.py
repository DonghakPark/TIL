"""
잃어버린 괄호 문제
author : donghak park
contact : donghark03@naver.com
"""

S = input().split('-')

answer = 0

for element in S[0].split('+'):
    answer += int(element)

for element in S[1:]:
    for sub in element.split('+'):
        answer -= int(sub)

print(answer)
