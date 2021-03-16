"""
셀프 넘버 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

self_num = [True] * 10001

for i in range(1, 100001):
    sum_i = 0

    temp = str(i)
    for element in temp:
        sum_i += int(element)

    index = i + sum_i

    if index <= 10000:
        self_num[index] = False

for i in range(1, len(self_num)):
    if self_num[i] is True:
        print(i)