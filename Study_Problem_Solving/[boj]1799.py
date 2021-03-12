"""
비숍 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""


### 브루트포스 풀이 >> 시간 초과
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# dx = [1,1,-1,-1]
# dy = [-1,1,-1,1]
#
# def possible(i, j, chess):
#     Q = deque()
#     for direct in range(4):
#         Q.append([direct,i, j])
#
#     visited = [[0] * N for _ in range(N)]
#     visited[i][j] = 1
#
#     while Q:
#         d, x, y = Q.popleft()
#
#         nx, ny = x + dx[d], y + dy[d]
#         if 0 <= nx < N and 0 <= ny < N:
#             if chess[nx][ny] == 2:
#                 return False
#             elif visited[nx][ny] == 0:
#                 Q.append([d, nx, ny])
#                 visited[nx][ny] = 1
#
#     return True
#
# def solution(count, chess):
#     global answer
#     global visited_chess
#
#     answer = max(answer, count)
#
#     for i in range(N):
#         for j in range(N):
#             if chess[i][j] == 1 and visited_chess[i][j] == 0:
#                 if possible(i, j, chess):
#                     chess[i][j] = 2
#                     visited_chess[i][j] = 1
#                     solution(count+1, chess)
#                     chess[i][j] = 1
#                     visited_chess[i][j] = 0
#
# N = int(input())
# chess0 = [list(map(int, input().split())) for _ in range(N)]
# chess1 = [[0] * N for _ in range(N)]
# chess2 = [[0] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if (i+j) % 2 == 1 and chess0[i][j] == 1:
#             chess1[i][j] = chess0[i][j]
#         elif (i+j) % 2 == 0 and chess0[i][j] == 1:
#             chess2[i][j] = chess0[i][j]
#
# visited_chess = [[0] * N for _ in range(N)]
# answer = -1
# solution(0, chess1)
# result = 0
# result += answer
# answer = -1
# solution(0, chess2)
# result += answer
# print(result)

# def check(idx):
#     c = idx % 2
#     i, j = idx // n, idx % n
#
#     for d in range(4):
#         x, y = i + dx[d], j + dy[d]
#         while 0 <= x < n and 0 <= y < n:
#             if visited[x * n + y]:
#                 return False
#             x += dx[d]
#             y += dy[d]
#     return True
#
#
# def dfs(idx, c, cnt):
#     if n * n - idx + 1 + cnt <= ans[c] or idx >= n * n:
#         return
#
#     ans[c] = max(ans[c], cnt)
#     x, y = idx // n, idx % n
#     j = y
#     for i in range(x, n):
#         while j < n:
#             v = i * n + j
#             if not visited[v] and chess[i][j] == 1 and check(v):
#                 visited[v] = True
#                 dfs(c, v, cnt + 1)
#                 visited[v] = False
#             j += 2
#         j = (c + 1) % 2 if i % 2 == 0 else c
#
#
# n = int(input())
# chess = [list(map(int, input().split())) for _ in range(n)]
# dx, dy = [1, -1, 1, -1], [1, 1, -1, -1]
# visited = [False] * (n ** 2)
# ans = [0, 0]
#
# dfs(0, 0, 0)
# dfs(1, 1, 0)
# print(sum(ans))
def check(idx):
    c = idx % 2
    i, j = idx // n, idx % n
    for d in range(4):
        x, y = i + dx[d], j + dy[d]
        while 0 <= x < n and 0 <= y < n:
            if visited[x * n + y]:
                return False
            x += dx[d]
            y += dy[d]
    return True


def dfs(idx, c, cnt):
    if n * n - idx + 1 + cnt <= ans[c] or idx >= n * n:
        return
    ans[c] = max(ans[c], cnt)
    x, y = idx // n, idx % n
    j = y
    for i in range(x, n):
        while j < n:
            v = i * n + j
            if not visited[v] and chess[i][j] == 1 and check(v):
                visited[v] = True
                dfs(v, c, cnt + 1)
                visited[v] = False
            j += 2
        j = (c + 1) % 2 if i % 2 == 0 else c


n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 1, -1], [1, 1, -1, -1]
visited = [False] * (n ** 2)
ans = [0, 0]
dfs(0, 0, 0)
dfs(1, 1, 0)
print(sum(ans))
