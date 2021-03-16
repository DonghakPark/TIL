"""
빠른 A+B 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A+B)