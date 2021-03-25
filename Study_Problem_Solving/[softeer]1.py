"""
8단 변속기 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

DCT_order = list(map(int, input().split()))

Ascending_order = sorted(DCT_order)
Descending_order = sorted(DCT_order, reverse=True)

if DCT_order == Ascending_order:
    print("ascending")
elif DCT_order == Descending_order:
    print("descending")
else:
    print("mixed")