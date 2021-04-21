"""
구갑 합 구하기 4 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0,arr[0]]
for i in range(1,len(arr)):
    sum_arr.append(sum_arr[i] + arr[i])

for _ in range(M):
    start, end = map(int, input().split())
    print(sum_arr[end] - sum_arr[start-1])
