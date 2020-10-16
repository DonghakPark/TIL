N, K = map(int, input().split())

arr = []
color = []

dx = [0,0,-1,1]
dy = [1,-1,0,0]
# 0: 흰색 1: 빨간색 2: 파란색

horse = [[[]]*N for _ in range(N)]

for _ in range(N):
    arr.append(list(map(int, input().split())))

for _ in range(K):
    i,j,k = (map(int, input().split()))
    color.append([i-1, j-1, k-1])

def move():


print(N)
print(K)
print(arr)
print(color)
print(horse)