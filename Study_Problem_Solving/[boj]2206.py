"""
벽 부수고 이동하기 문제
author : donghak park
contact: donghark03@naver.com
"""

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, list(input()))))

