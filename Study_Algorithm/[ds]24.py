# 낚시왕
R, C, M = map(int, input().split())

shark = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]

# r,c,s,d,z ( x , y , 속력, 방향, 크기 )
for _ in range(M):
    shark.append(list(map(int,input().split())))

# 상어의 위치를 저장 하는 배열
fish_map = [[[] for _ in range(C) ] for _ in range(R)]

for r,c,s,d,z in shark:
    fish_map[r-1][c-1].append([s,d,z])

print(shark)
print(fish_map)