"""
마법사 상어와 비바라기
Author : DongHak Park
"""
import sys
from collections import deque

input = sys.stdin.readline
# 1부터 시작
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]

N, M = map(int, input().split())

cloud_map = []
for _ in range(N):
    cloud_map.append(list(map(int, input().split())))

commands = []
for _ in range(M):
    commands.append(list(map(int, input().split())))

cloud = deque([[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]])

for command in commands:
    now_d, now_s = command
    now_d = now_d - 1

    visited = [[False] * N for _ in range(N)]

    # 1
    qlen = len(cloud)
    while qlen > 0:
        x, y = cloud.popleft()

        nx, ny = (x + (dx[now_d] * now_s)) % N, (y + (dy[now_d] * now_s)) % N

        cloud.append([nx, ny])
        qlen -= 1
    # 2
    for x, y in cloud:
        cloud_map[x][y] += 1
        visited[x][y] = True
    # 3
    for x, y in cloud:
        bucket_cnt = 0

        for i in range(4):
            nx, ny = x + dx2[i], y + dy2[i]

            if 0 <= nx < N and 0 <= ny < N and cloud_map[nx][ny] > 0:
                bucket_cnt += 1

        cloud_map[x][y] += bucket_cnt

    cloud.clear()

    for i in range(N):
        for j in range(N):
            if cloud_map[i][j] >= 2 and visited[i][j] is False:
                cloud.append([i, j])
                cloud_map[i][j] -= 2

answer = 0

for element in cloud_map:
    answer += sum(element)

print(answer)
