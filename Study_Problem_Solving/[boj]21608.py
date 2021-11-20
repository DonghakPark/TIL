"""
상어 초등학교
Author : DongHak Park
"""
from collections import defaultdict

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())

assigned = [[-1] * N for _ in range(N)]
answer = 0
student = defaultdict(list)
order = []

for _ in range(N ** 2):
    st, a1, a2, a3, a4 = map(int, input().split())
    student[st].extend([a1, a2, a3, a4])
    order.append(st)

for st_num in order:
    favor = []
    max_blank = -1
    max_faver = -1
    for x in range(N):
        for y in range(N):
            blank_cnt = 0
            favor_cnt = 0
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and assigned[x][y] == -1:
                    if assigned[nx][ny] == -1:
                        blank_cnt += 1
                    if assigned[nx][ny] in student[st_num]:
                        favor_cnt += 1

            if (favor_cnt >= max_faver or blank_cnt >= max_blank) and assigned[x][y] == -1:
                favor.append([favor_cnt, blank_cnt, x, y])
            max_blank, max_faver = max(max_blank, blank_cnt), max(max_faver, favor_cnt)

    favor.sort(key=lambda t: (-t[0], -t[1], t[2], t[3]))

    ass_x, ass_y = favor[0][2], favor[0][3]
    assigned[ass_x][ass_y] = st_num

for x in range(N):
    for y in range(N):
        favor_cnt = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if assigned[nx][ny] in student[assigned[x][y]]:
                    favor_cnt += 1
        if favor_cnt == 0:
            answer += 0
        elif favor_cnt == 1:
            answer += 1
        elif favor_cnt == 2:
            answer += 10
        elif favor_cnt == 3:
            answer += 100
        elif favor_cnt == 4:
            answer += 1000
print(answer)
