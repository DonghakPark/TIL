"""
금고털이 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
import sys

jew = [0] * 10001
W, N = map(int, input().split())
for _ in range(N):
    now_w, now_p = map(int, input().split())
    jew[now_p] += now_w

total_w = 0
total_p = 0
for i in range(10000, -1, -1):
    if jew[i] != 0:
        if jew[i] >= (W-total_w):
            total_p += (W-total_w) * i
            break
        else:
            total_p += jew[i] * i
            total_w += jew[i]
print(total_p)
