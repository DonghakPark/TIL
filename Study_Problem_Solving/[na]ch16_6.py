"""
편집 거리 문제
author : donghak park
contact : donghark03@naver.com
"""
S1 = list(input())
S2 = list(input())

count_remove = 0
count_add = 0

alpha_S1 = [0] * 26
alpha_S2 = [0] * 26

for element in S1:
    alpha_S1[ord(element) - 97] += 1

for element in S2:
    alpha_S2[ord(element) - 97] += 1

print(alpha_S1)
print(alpha_S2)

for ori,tar in zip(alpha_S1, alpha_S2):
    if ori > tar:
        count_remove += 1
    elif ori < tar:
        count_add += 1

print(max(count_add,count_remove))