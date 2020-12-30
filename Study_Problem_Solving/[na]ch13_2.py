"""
연구소 문제
author : donghak park
contact : donghark03@naver.com
"""
import copy

N, M = map(int, input().split())
# N -> 행 M -> 열

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def doit(arr,virus):
    temp = copy.deepcopy(arr)
    vi = copy.deepcopy(virus)

    while vi:
        x,y = vi.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < N and ny < M and nx >=0 and ny >=0:
                if temp[nx][ny] == 0:
                    vi.append([nx,ny])
                    temp[nx][ny] = 2
    local_answer = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                local_answer += 1
    return local_answer

virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append([i,j])

answer = -2e9
count = 0

def make_wall(count):
    global answer

    if count == 3:
        temp = doit(arr,virus)
        answer = max(answer, temp)
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                count += 1
                make_wall(count)
                arr[i][j] = 0
                count -= 1

make_wall(0)
print(answer)