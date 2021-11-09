"""
낚시왕 문제
Author : DongHak Park
"""
import copy, sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

R, C, M = map(int, input().split())

if M == 0:
    print(0)
    sys.exit()

pool = {}
for i in range(R):
    for j in range(C):
        pool[(i, j)] = []

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    # s: 속력, d: 이동 방향, z: 크기
    if d == 1 or d == 2:
        s = s % ((R - 1) * 2)
    else:
        s = s % ((C - 1) * 2)
    pool[(r - 1, c - 1)].append([z, s, d - 1])

now_person_col = -1
answer = 0

while now_person_col < C - 1:
    # 오른쪽으로 한칸 이동
    now_person_col += 1

    # 가장 가까운 상어 잡기
    for i in range(R):
        if pool[(i, now_person_col)]:
            size, s, d = pool[(i, now_person_col)].pop()
            answer += size
            break
    temp = []

    # 상어 이동
    for i in range(R):
        for j in range(C):

            while pool[(i, j)]:
                now_x, now_y = i, j
                now_z, now_s, now_d = pool[(i, j)].pop()

                for count in range(now_s):
                    nx, ny = now_x + dx[now_d], now_y + dy[now_d]

                    if 0 <= nx < R and 0 <= ny < C:
                        now_x, now_y = nx, ny
                    else:
                        if now_d == 0:
                            now_d = 1
                        elif now_d == 1:
                            now_d = 0
                        elif now_d == 2:
                            now_d = 3
                        else:
                            now_d = 2

                        now_x, now_y = now_x + dx[now_d], now_y + dy[now_d]

                temp.append([now_x, now_y, now_z, now_s, now_d])

    for element in temp:
        pool[(element[0], element[1])].append([element[2], element[3], element[4]])

    # 겹치는 상어 삭제
    for i in range(R):
        for j in range(C):
            if pool[(i, j)]:
                pool[(i, j)].sort(reverse=True)
                pool[(i, j)] = pool[(i, j)][:1]

print(answer)
