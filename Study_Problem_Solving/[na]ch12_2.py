"""
문자열 재정렬 문제
author : donghak park
contact : donghark03@naver.com
"""

S = list(input())
sum = 0
s_arr = []

for element in S:
    if element.isalpha() is True:
        s_arr.append(element)
    else:
        sum += int(element)

s_arr.sort()
print(''.join(s_arr) + str(sum))
