"""
주사위 굴리기 2
Author : Donghak Park
"""

"""
정육면체 굴리기 문제
Author : DongHak Park
"""
from collections import deque

def rolling(d):
    global dice

    new_dice = [0,0,0,0,0,0]
    if d == 0:
        new_dice[0] = dice[2]
        new_dice[1] = dice[0]
        new_dice[2] = dice[5]
        new_dice[3] = dice[3]
        new_dice[4] = dice[4]
        new_dice[5] = dice[1]
    elif d == 1:
        new_dice[0] = dice[3]
        new_dice[1] = dice[1]
        new_dice[2] = dice[2]
        new_dice[3] = dice[5]
        new_dice[4] = dice[0]
        new_dice[5] = dice[4]
    elif d == 2:
        new_dice[0] = dice[1]
        new_dice[1] = dice[5]
        new_dice[2] = dice[0]
        new_dice[3] = dice[3]
        new_dice[4] = dice[4]
        new_dice[5] = dice[2]
    elif d == 3:
        new_dice[0] = dice[4]
        new_dice[1] = dice[1]
        new_dice[2] = dice[2]
        new_dice[3] = dice[0]
        new_dice[4] = dice[5]
        new_dice[5] = dice[3]

    dice = new_dice[::]

def get_score(x, y):
    global answer

    now_num = arr[x][y]
    num_cnt = 1

    visited = [[False] * M for _ in range(N)]

    Q = deque()
    Q.append([x,y])
    visited[x][y] = True

    while Q:
        now_x, now_y = Q.popleft()

        for i in range(4):
            next_x, next_y = now_x + dx[i], now_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M and visited[next_x][next_y] is False:
                if arr[next_x][next_y] == now_num:
                    num_cnt += 1
                    Q.append([next_x, next_y])
                    visited[next_x][next_y] = True
    answer += (now_num * num_cnt)

dice = [1,2,5,4,3,6]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


now_x, now_y, now_d = 0,0,1
answer = 0
for _ in range(K):
    next_x, next_y = now_x + dx[now_d], now_y + dy[now_d]

    if 0 <= next_x < N and 0 <= next_y < M:
        rolling(now_d)

    else:
        now_d = (now_d + 2) % 4
        rolling(now_d)
        next_x, next_y = now_x + dx[now_d], now_y + dy[now_d]

    now_x, now_y = next_x, next_y
    get_score(now_x, now_y)

    if dice[5] > arr[now_x][now_y]:
        now_d = (now_d + 1) % 4
    elif dice[5] < arr[now_x][now_y]:
        now_d = (now_d - 1) % 4

print(answer)


