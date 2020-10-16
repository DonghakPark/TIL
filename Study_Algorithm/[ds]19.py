#원판 돌리기 문제
"""
원판을 아래와 같은 방법으로 총 T번 회전시키려고 한다. 원판의 회전 방법은 미리 정해져 있고, i번째 회전할때 사용하는 변수는 xi, di, ki이다.

번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
"""
from array import ArrayType

N, M, T = map(int, input().split())

Arr = []
#N개의 원판
for _ in range(N):
    Arr.append(list(map(int, input().split())))

Rotate = []
for _ in range(T):
    Rotate.append(list(map(int, input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]
for x,d,k in Rotate:

    print("Before",Arr)
    for i in range(len(Arr)):
        if (i + 1) % x == 0:

            if d == 0:
                for _ in range(k):
                    temp = Arr[i].pop()
                    Arr[i].insert(0,temp)
            elif d == 1:
                for _ in range(k):
                    temp = Arr[i].pop(0)
                    Arr[i].append(temp)

    count = 0
    s = 0

    for i in range(N):
        for j in range(M):
            if Arr[i][j] == 0:
                count +=1
            s += Arr[i][j]

    if count != N*M:
        flag2 = False
        candidate = []

        for i in range(N):
            for j in range(M):

                for z in range(4):
                    nx = (i + dx[z])
                    ny = (j + dy[z]) % M

                    if nx < N and nx >= 0:
                        if Arr[i][j] == Arr[nx][ny] and Arr[i][j] != 0:
                            flag2 = True
                            if [nx,ny] in candidate:
                                continue
                            else:
                                candidate.append([nx,ny])

        for x,y in candidate:
            Arr[x][y] = 0

        if flag2 == False:

            avg = s/((N*M)-count)
            for i in range(N):
                for j in range(M):
                    if Arr[i][j] != 0:
                        if Arr[i][j] > avg:
                            Arr[i][j] -= 1
                        elif Arr[i][j] < avg:
                            Arr[i][j] += 1
    else:
        break

answer = 0
for i in range(N):
    for j in range(M):
        answer += Arr[i][j]
print(answer)








