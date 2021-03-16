"""
수 정렬하기 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort()

for element in arr:
    print(element)