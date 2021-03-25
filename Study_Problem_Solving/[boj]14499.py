"""
주사위 굴리기 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""


def move_dice(d):
    global dice
    # 동쪽으로
    if d == 0:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    # 서쪽으로
    elif d == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    # 북쪽으로
    elif d == 2:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    # 남쪽으로
    else:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]


N, M, x, y, k = map(int, input().split())
dice_map = []

for _ in range(N):
    dice_map.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0, 0]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

now_x, now_y = x, y

for command in commands:
    direct = command - 1

    nx, ny = now_x + dx[direct], now_y + dy[direct]

    if 0 <= nx < N and 0 <= ny < M:
        move_dice(direct)

        if dice_map[nx][ny] == 0:
            dice_map[nx][ny] = dice[1]
        else:
            dice[1] = dice_map[nx][ny]
            dice_map[nx][ny] = 0

        now_x, now_y = nx, ny
        print(dice[6])