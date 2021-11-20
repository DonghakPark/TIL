"""
마법사 상어와 토네이도
Author : DongHak Park
"""
from collections import deque
import math

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N = int(input())
answer = 0
sand_map = []

for _ in range(N):
    sand_map.append(list(map(int, input().split())))

now_move_dist = 1
left_dist = 0
now_dir = 0

turn_time = 0
turn_dist = 1

now_x, now_y = N // 2, N // 2
# ratio_dict = { (-1, 1): 0.01, (1, 1): 0.01, (-1, 0): 0.07, (-2, 0): 0.02,
#     (1, 0): 0.07, (2, 0): 0.02, (-1, -1): 0.1, (1, -1): 0.1, (0, -2): 0.05 }

ratio = {
    0: {(-1, 1): 0.01, (1, 1): 0.01, (-1, 0): 0.07, (-2, 0): 0.02,
        (1, 0): 0.07, (2, 0): 0.02, (-1, -1): 0.1, (1, -1): 0.1, (0, -2): 0.05},

    1: {(-1, -1): 0.01, (-1, 1): 0.01, (0, -1): 0.07, (0, -2): 0.02,
        (0, 1): 0.07, (0, 2): 0.02, (1, -1): 0.1, (1, 1): 0.1, (2, 0): 0.05},

    2: {(-1, -1): 0.01, (1, -1): 0.01, (-1, 0): 0.07, (-2, 0): 0.02,
        (1, 0): 0.07, (2, 0): 0.02, (1, 1): 0.1, (-1, 1): 0.1, (0, 2): 0.05},

    3: {(1, -1): 0.01, (1, 1): 0.01, (0, 1): 0.07, (0, 2): 0.02,
        (0, -1): 0.07, (0, -2): 0.02, (-1, -1): 0.1, (-1, 1): 0.1, (-2, 0): 0.05}

}

route = deque()

route.append([now_x, now_y, left_dist])

sum_temp = 0

while True:
    now_x, now_y, left_dist = route.popleft()

    if now_x == 0 and now_y == 0:
        break

    if left_dist == now_move_dist:
        left_dist = 0
        turn_time += 1
        now_dir = (now_dir + 1) % 4
        if turn_time % 2 == 0:
            now_move_dist += 1

    # 이동
    next_x = now_x + dx[now_dir]
    next_y = now_y + dy[now_dir]
    local_d = now_dir

    route.append([next_x, next_y, left_dist + 1])

    sum_sand = 0
    dist_sand = sand_map[next_x][next_y]

    for key in ratio[local_d].keys():

        move_x, move_y = key

        target_x, target_y = next_x + move_x, next_y + move_y
        move_sand = math.trunc(dist_sand * ratio[local_d][key])

        if 0 <= target_x < N and 0 <= target_y < N:
            sand_map[target_x][target_y] += move_sand
            sum_sand += move_sand
        else:
            answer += move_sand
            sum_sand += move_sand

    if 0 <= next_x + dx[local_d] < N and 0 <= next_y + dy[local_d] < N:
        sand_map[next_x + dx[local_d]][next_y + dy[local_d]] += sand_map[next_x][next_y] - sum_sand
        sand_map[next_x][next_y] = 0
    else:
        answer += sand_map[next_x][next_y] - sum_sand
        sand_map[next_x][next_y] = 0
sum_temp = 0

print(answer)
