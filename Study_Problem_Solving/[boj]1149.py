"""
RGB 거리 문제
author : donghak park
contact: donghark03@naver.com
"""
import sys
input = sys.stdin.readline

def solution():
    global arr

    for i in range(1, N):
        arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + arr[i][0]
        arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1]
        arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2]

    return min(arr[N-1][0], arr[N-1][1], arr[N-1][2])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(solution())