# """
# 게임 개발 문제
# """
#
# N,M = map(int, input().split())
# y,x,d = map(int, input().split())
#
# arr = []
# visited = [[ False for _ in range(M)]  for _ in range(N)]
# visited[x][y] = True
#
# for i in range(N):
#     arr.append(list(map(int, input().split())))
#
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
#
# while True:
#
#     flag = False
#
#     for i in range(1,5):
#         # 왼쪽을 바라본다
#         d = (d-i)%4
#
#         nx = x + dx[d]
#         ny = y + dy[d]
#
#         if visited[nx][ny] == False and arr[nx][ny] == 0:
#             x = nx
#             y = ny
#             flag = True
#         else:
#             continue
#
#     if flag == False:
#         nx = x - dx[d]
#         ny = y - dy[d]
#         if arr[nx][ny] == 1:
#             break
#         else:
#             x = nx
#             y = ny
#
#
#
#

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x,y,direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)