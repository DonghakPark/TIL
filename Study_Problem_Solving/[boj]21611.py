"""
마법사 상어와 블리자드
Author : DongHak Park
"""
import sys
from collections import deque
input = sys.stdin.readline

def display(str):
    global arr

    print("now :",str)
    for element in arr:
        print(*element)
    print("-----------------------")

def magic(d, s):
    global arr
    x, y = start_pos, start_pos
    for _ in range(s):
        nx, ny = x + magic_dx[d], y + magic_dy[d]

        if 0 <= nx < N and 0 <= ny < N:
            arr[nx][ny] = 0
            x, y = nx, ny

def move1():
    global arr

    new_arr = deque()

    Q = deque()
    Q.append([start_pos, start_pos])
    move_cnt = 1
    len_cnt = 1

    now_d = 0

    while Q:
        now_x, now_y = Q.popleft()
        nx, ny = now_x + move_dx[now_d], now_y + move_dy[now_d]

        move_cnt -= 1
        if 0 <= nx < N and 0 <= ny < N:
            Q.append([nx, ny])
            if arr[nx][ny] != 0:
                new_arr.append(arr[nx][ny])

        if move_cnt == 0:
            now_d = (now_d + 1) % 4
            if now_d % 2 == 0:
                len_cnt += 1
            move_cnt = int(len_cnt)

    Q = deque()
    Q.append([start_pos, start_pos])
    move_cnt = 1
    len_cnt = 1
    now_d = 0

    while Q:
        now_x, now_y = Q.popleft()
        nx, ny = now_x + move_dx[now_d], now_y + move_dy[now_d]

        move_cnt -= 1
        if 0 <= nx < N and 0 <= ny < N:
            Q.append([nx, ny])
            if new_arr:
                element = new_arr.popleft()
                arr[nx][ny] = int(element)
            else:
                arr[nx][ny] = 0

        if move_cnt == 0:
            now_d = (now_d + 1) % 4
            if now_d % 2 == 0:
                len_cnt += 1
            move_cnt = int(len_cnt)

def explosion():
    global arr
    global answer

    Q = deque()
    Q.append([start_pos, start_pos])
    move_cnt = 1
    len_cnt = 1
    now_d = 0

    explosion_cnt = 0

    now_sequence = []
    now_flag = arr[start_pos][start_pos-1]
    while Q:
        now_x, now_y = Q.popleft()
        nx, ny = now_x + move_dx[now_d], now_y + move_dy[now_d]

        move_cnt -= 1

        if 0 <= nx < N and 0 <= ny < N:
            Q.append([nx, ny])
            if arr[nx][ny] == now_flag:
                now_sequence.append([nx,ny])
            else:
                if len(now_sequence) >= 4:
                    for x1, y1 in now_sequence:
                        arr[x1][y1] = 0
                    explosion_cnt += 1
                    answer += len(now_sequence) * now_flag
                now_sequence.clear()
                now_sequence.append([nx, ny])
                now_flag = arr[nx][ny]

        if move_cnt == 0:
            now_d = (now_d + 1) % 4
            if now_d % 2 == 0:
                len_cnt += 1
            move_cnt = int(len_cnt)
    if explosion_cnt == 0:
        return
    else:
        move1()
        explosion()

def remake():
    global arr

    Q = deque()
    Q.append([start_pos, start_pos])
    move_cnt = 1
    len_cnt = 1
    now_d = 0

    new_group = deque()

    now_sequence = 0
    now_flag = arr[start_pos][start_pos-1]
    while Q:
        now_x, now_y = Q.popleft()
        nx, ny = now_x + move_dx[now_d], now_y + move_dy[now_d]

        move_cnt -= 1

        if 0 <= nx < N and 0 <= ny < N:
            Q.append([nx, ny])
            if arr[nx][ny] == now_flag:
                now_sequence += 1
            else:
                if now_sequence == 0:
                    new_group.extend([1, now_flag])
                else:
                    new_group.extend([now_sequence, now_flag])
                now_sequence = 1
                now_flag = arr[nx][ny]

        if move_cnt == 0:
            now_d = (now_d + 1) % 4
            if now_d % 2 == 0:
                len_cnt += 1
            move_cnt = int(len_cnt)
    Q = deque()
    Q.append([start_pos, start_pos])
    move_cnt = 1
    len_cnt = 1
    now_d = 0

    while Q and new_group:
        now_x, now_y = Q.popleft()
        nx, ny = now_x + move_dx[now_d], now_y + move_dy[now_d]

        move_cnt -= 1
        new_element = new_group.popleft()

        if 0 <= nx < N and 0 <= ny < N:
            Q.append([nx, ny])
            arr[nx][ny] = new_element


        if move_cnt == 0:
            now_d = (now_d + 1) % 4
            if now_d % 2 == 0:
                len_cnt += 1
            move_cnt = int(len_cnt)

# input
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]
commands = deque(commands)
start_pos = ((N+1)//2) - 1
magic_dx = [-1,1,0,0]
magic_dy = [0,0,-1,1]
move_dx = [0,1,0,-1]
move_dy = [-1,0,1,0]
answer = 0

while commands:
    now_d, now_s = commands.popleft()

    magic(now_d-1, now_s)
    move1()
    explosion()
    remake()

print(answer)