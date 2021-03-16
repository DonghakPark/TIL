"""
사분면 고르기 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

x = int(input())
y = int(input())

if x >= 0:
    if y >= 0:
        print(1)
    else:
        print(4)
else:
    if y >= 0:
        print(2)
    else:
        print(3)
