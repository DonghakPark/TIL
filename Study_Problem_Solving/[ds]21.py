# #새로운 게임 2
# N, K = map(int, input().split())
#
# arr = []
# horse = []
# upon = []
#
# dx = [0,0,-1,1]
# dy = [1,-1,0,0]
# # 0: 흰색 1: 빨간색 2: 파란색
#
# upon = [[[]]*N for _ in range(N)]
#
# for _ in range(N):
#     arr.append(list(map(int, input().split())))
#
# for num in range(K):
#     i,j,k = (map(int, input().split()))
#     horse.append([num, i-1, j-1, k-1])
#
# for i in range(K):
#     num, x, y, d = horse[i]
#     upon[x][y].append([num,x,y,d])
# # 처음 상태 저장
#
#
# def make_group():
#
# def move(num,x,y,d):
#
#     nx = x + dx[d]
#     ny = y + dy[d]
#
#     if nx < 0 or ny < 0 or nx >=N or ny >= N or arr[nx][ny] == 2:
#         d = (d+2)%2
#         temp = upon[nx][ny][]
#
#
#
#
# print(N)
# print(K)
# print(arr)
# print(upon)
#
import sys

input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def move(chess_num):
    x, y, z = chess[chess_num]
    nx = x + dx[z]
    ny = y + dy[z]

    if not 0 <= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
        if 0<=z <=1:
            nz = (z+1) %2
        else:
            nz = (z-1)%2 + 2
        chess[chess_num][2] = nz

        nx = x + dx[z]
        ny = y + dy[z]
        if not 0 <= nx < n or not 0 <= ny < n or a[nx][ny] == 2:
            return 0
    chess_set = []
    for i, key in enumerate(chess_map[x][y]):
        if key == chess_num:
            chess_set.extend(chess_map[x][y][i:])
            chess_map[x][y] = chess_map[x][y][:i]

    if a[nx][ny] == 1:
        chess_set = chess_set[-1::-1]

    for i in chess_set:
        chess_map[nx][ny].append(i)
        chess[i][:2] = [nx,ny]

    if len(chess_map[nx][ny]) >= 4:
        return 1
    return 0

n, k = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]
chess_map = [[[] for _ in range(n)] for _ in range(n)]
chess = [0 for _ in range(k)]

for i in range(k):
    x, y, z = map(int, input().split())
    chess_map[x-1][y-1].append(i)
    chess[i] = [x-1,y-1,z-1]

cnt = 1
while cnt <= 1000:
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit()
    cnt += 1
print(-1)