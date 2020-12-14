#주사위 굴리기


# input 처리 부분
N, M, x, y, K = map(int, input().split())

map_list = []

for row in range(N):
    map_list.append(list(map(int, input().split())))

orders = map(int, input().split())

d_row = [0,0,-1,1]
d_col = [1,-1,0,0]

dice = [[0,0,0,0],[0,0,0,0]]

up = 1
rolling = 0

for order in orders:
    next_x = x + d_row[order-1]
    next_y = y + d_col[order-1]

    if (next_x < 0) or (next_x >= N) or (next_y < 0) or (next_y >= M):
        continue

    else:

        if order == 1:
            rolling = 1

            temp = dice[rolling].pop(0)
            dice[rolling].append(temp)

            temp2 = dice[rolling][1]
            dice[rolling - 1][1] = temp2

        elif order == 2:
            rolling = 0
            temp = dice[rolling].pop()
            dice[rolling].insert(0, temp)

            temp2 = dice[rolling][1]
            dice[rolling + 1][1] = temp2

        elif order == 3:
            rolling = 1

            temp = dice[rolling].pop()
            dice[rolling].insert(0,temp)

            temp2 = dice[rolling][1]
            dice[rolling - 1][1] = temp2

        else:
            rolling = 0

            temp = dice[rolling].pop(0)
            dice[rolling].append(temp)

            temp2 = dice[rolling][1]
            dice[rolling + 1][1] = temp2

        if map_list[next_x][next_y] == 0:
            map_list[next_x][next_y] = dice[rolling][3]
        else:
            dice[rolling][3] = map_list[next_x][next_y]
            map_list[next_x][next_y] = 0

        print(dice[rolling][1])

        x = next_x
        y = next_y