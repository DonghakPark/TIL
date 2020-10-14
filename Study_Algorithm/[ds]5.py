# # 아기 상어
# # BFS --> queue를 이용한 구현이 핵심
# # 거리를 기록하자
# '''
# N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.
#
# 아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다.
# 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
#
# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
# 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
#
# 아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.
#
# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.
#
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
#
# 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
# '''
# N = int(input())
#
# Arr = []
#
# for _ in range(N):
#     Arr.append(list(map(int, input().split())))
#
# size = 2
#
# dist = [[-1]* N for i in range(N)]
#
# fish = []
# shark = []
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# def find_fish():
#     global shark
#     global fish
#
#     temp = []
#
#     for i in range(N):
#         for j in range(N):
#             if Arr[i][j] == 9:
#                 shark = [i,j]
#             elif Arr[i][j] != 0:
#                 temp.append([i,j,Arr[i][j]])
#
#     fish = temp
#
# def find_path(x, y, x_e, y_e):
#     global dist
#
#     Q = []
#     Q.append([x,y])
#     dist[x][y] = 0
#
#     while Q:
#
#         x_1, y_1 = Q.pop(0)
#         distance = dist[x_1][y_1]
#         if x_1 == x_e and y_1 == y_e:
#
#             return [x_e, y_e, distance]
#
#         for i in range(4):
#             nx = x_1 + dx[i]
#             ny = y_1 + dy[i]
#
#             if nx >= N or ny >= N or nx < 0 and ny < 0:
#                 continue
#
#             if Arr[nx][ny] > size:
#                 continue
#
#             if dist[nx][ny] == 1 or distance + 1 < dist[nx][ny]:
#                 dist[nx][ny] = distance + 1
#                 Q.append([nx,ny])
#
#             if dist[nx][ny] == -1 and Arr[nx][ny] <= size:
#                 dist[nx][ny] = distance +1
#                 Q.append([nx,ny])
#
# time = 0
# ate = 0
#
# while True:
#
#     find_fish()
#     fish.sort(key=lambda x: x[2])
#
#     if len(fish) == 0:
#         break
#     elif fish[0][2] >= size:
#         break
#
#     else:
#         temp = []
#         for f in fish:
#             dist = [[-1] * N for i in range(N)]
#             if f[2] < size:
#                 result = find_path(shark[0],shark[1],f[0],f[1])
#                 temp.append(result)
#
#         temp.sort(key = lambda x : (x[2], x[0], x[1]))
#
#         f_x, f_y, f_d = temp.pop(0)
#
#         Arr[f_x][f_y] = 9
#         Arr[shark[0]][shark[1]] = 0
#         ate += 1
#         time += f_d
#
#         print(f_x, f_y, f_d)
#     if ate >= size:
#         size += 1
#         ate = 0
#
# print(time)

from collections import deque
INF = 1e9 #10억을 의미한다

n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

now_size = 2
now_x, now_y = 0,0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i,j
            array[now_x][now_y] = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    dist = [[-1] * n for _ in range(n)]

    q = deque([(now_x,now_y)])
    dist[now_x][now_y] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist

def find(dist):
    x,y = 0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):

            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x, y = i,j
                    min_dist = dist[i][j]

    if min_dist == INF:
        return None
    else:
        return x,y,min_dist

result = 0
ate = 0

while True:
    value = find(bfs())

    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]

        array[now_x][now_y] = 0
        ate += 1

        if ate >= now_size:
            now_size += 1
            ate = 0