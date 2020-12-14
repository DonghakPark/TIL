# 나무 재테크

"""
봄에는 자신의 나이만큼 양분을 먹음 나이 1증가
한칸에 여러 나무가 있으면 어린 나무 부터 섭취
양분을 먹지 못하면 즉시 죽는다.

여름에는 봄에 죽은 나무 나이 /2 만큼 양분으로 된다.

가을 주위 8칸에 레벨 1짜리 애기 나무들 생성

겨울 로봇이 양분 주고 다님

K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.

"""

N, M, K = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

en = [[5] * N for _ in range(N)]

tree = {}
for _ in range(M):
    temp = list(map(int, input().split()))
    temp[0] -= 1
    temp[1] -= 1
    tree[temp[0],temp[1]] = [temp[2]]

dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

for year in range(K):
    for i in tree:
        tree[i].sort()

    summer = []

    for x, y in tree:
        temp = []

        while tree[x,y]:


            if sum(tree[x, y]) > en[x][y]:
                last_t = tree[x, y].pop()
                summer.append([x, y, last_t])
                continue

            else:
                last_t = tree[x, y].pop()
                en[x][y] = en[x][y] - last_t
                temp.append(last_t + 1)

        tree[x,y] = temp

    for element in summer:
        en[element[0]][element[1]] += int(element[2] / 2)

    for i in range(8):
        for x,y in tree:
            nx = x + dx[i]
            ny = y + dy[i]

            check = tree.keys()

            if nx < N and ny < N and ny >=0 and nx >=0:
                if (nx,ny) in check:
                    tree[nx,ny].append(1)
                else:
                    tree[nx,ny] = [1]

    for i in range(N):
        for j in range(N):
            en[i][j] += A[i][j]


count = 0

for x,y in tree:
    count += len(tree[x,y])


print(count)




