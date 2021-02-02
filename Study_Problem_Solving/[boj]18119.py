"""
단어 암기 문제
author : donghak park
contact: donghark03@naver.com
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

dp[0][0][1] = 1

for i in range(2, N):
    if arr[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for r in range(1, N):
    for c in range(1, N):
        if arr[r][c] == 0 and arr[r][c-1] == 0 and arr[r-1][c] == 0:
            dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

        if arr[r][c] == 0:
            dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1]
            dp[2][r][c] = dp[2][r-1][c] + dp[1][r-1][c]

print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])


"""
또 다른 풀이 ( 시간 초과남 )
def search(x, y, direct):
    global answer

    if x == N-1 and y == N-1:
        answer += 1
        return

    if direct == 0 or direct == 1 or direct == 2:
        if x + 1 < N and y + 1 < N:
            if arr[x + 1][y] == 0 and arr[x + 1][y + 1] == 0 and arr[x][y + 1] == 0:
                search(x+1, y+1, 2)

    if direct == 0 or direct == 2:
        if y + 1 < N:
            if arr[x][y + 1] == 0:
                search(x, y+1, 0)

    if direct == 1 or direct == 2:
        if x + 1 < N:
            if arr[x + 1][y] == 0:
                search(x+1, y, 1)
"""
