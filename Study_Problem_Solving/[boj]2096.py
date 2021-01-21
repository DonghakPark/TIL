"""
내려가기 문제
author : donghak park
contact: donghark03@naver.com
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = []
arr_max = [[0,0,0],[0,0,0]]
arr_min = [[0,0,0],[0,0,0]]

for _ in range(N):
    A,B,C = list(map(int, input().split()))
    arr.append([A,B,C])

for i in range(0,N):

    arr_max[1][0] = max(arr_max[0][1], arr_max[0][0]) + arr[i][0]
    arr_max[1][1] = max(arr_max[0][1], arr_max[0][2], arr_max[0][0]) + arr[i][1]
    arr_max[1][2] = max(arr_max[0][1], arr_max[0][2]) + arr[i][2]

    arr_min[1][0] = min(arr_min[0][0], arr_min[0][1]) + arr[i][0]
    arr_min[1][1] = min(arr_min[0][1], arr_min[0][2], arr_min[0][0]) + arr[i][1]
    arr_min[1][2] = min(arr_min[0][1], arr_min[0][2]) + arr[i][2]

    arr_max.append(arr_max.pop(0))
    arr_min.append(arr_min.pop(0))

print(max(arr_max[0]), end=" ")
print(min(arr_min[0]))