# 드래곤 커브

N = int(input())

curve = []

# x,y == 시작점 , d = 시작 방향, g는 세대
for _ in range(N):
    curve.append(list(map(int, input().split())))
print(curve)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

