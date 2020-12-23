"""
만들 수 없는 금액 문제
"""
from itertools import combinations

N = int(input())
coin = list(map(int, input().split()))

coin.sort() #sorting
sheet = []

for i in range(1, len(coin)+1):
    temp = list(list(combinations(coin,i)))

    for element in temp:
        if sum(element) not in sheet:
            sheet.append(sum(element))
sheet.sort()

answer = 1
while True:
    if answer in sheet:
        answer += 1
    else:
        print(answer)
        break
"""
책 풀이
-> 해답을 찾는 방식이 이해가 쉽지 않음
"""

# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# target = 1
# for x in data:
#     if target < x:
#         break
#     target += x
#
# print(target)