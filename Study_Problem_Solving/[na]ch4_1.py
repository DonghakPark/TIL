# N = int(input())
# cmd = list(input().split())
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# for i in range(len(cmd)):
#     if cmd[i] == "L":
#         cmd[i] = 0
#     elif cmd[i] == "R":
#         cmd[i] = 1
#     elif cmd[i] == "U":
#         cmd[i] = 2
#     else:
#         cmd[i] = 3
#
# x,y = 1,1
# for element in cmd:
#     nx = x + dx[element]
#     ny = y + dy[element]
#
#     if nx>=1 and nx <= N and ny >= 1 and ny <= N:
#         x = nx
#         y = ny
#
# print(x,y)

n = int(input())
x, y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:

    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n and ny > n:
        continue
    x, y = nx, ny

print(x,y)
