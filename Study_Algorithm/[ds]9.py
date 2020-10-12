# 로본 청소기

N, M = map(int,input().split())

x, y, d = map(int,input().split())

ori = []

for _ in range(N):
    ori.append(list(map(int, input().split())))

print(ori)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:

    if ori[x][y] == 0:
        ori[x][y] == 2 # 청소는 2

