# 게리멘더링 2

N = int(input())

Arr_popul = []
for _ in range(N):
    Arr_popul.append(list(map(int, input().split())))

answer = 1e9

# 결과 값은 최소값 출력

def find_line(x,y,d1,d2):

    diff = [0] * 5

    Arr_map = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N):

            if 0 <= i < x+d1 and 0 <= j <= y:
                Arr_map[i][j] = 1
            elif 0 <= i <= x+d2 and y < j < N:
                Arr_map[i][j] = 2
            elif x+d1 <= i < N and 0 <= j < y-d1+d2:
                Arr_map[i][j] = 3
            elif x+d2 < i < N and y-d1+d2 <= j < N:
                Arr_map[i][j] = 4
            # 5번 선거구인 경우
    for i in range(d1+1):
        Arr_map[x+i][y-i] = 5
        Arr_map[x+d2+i][y+d2-i] = 5

    for i in range(d2+1):
        Arr_map[x+i][y+i] = 5
        Arr_map[x+d1+i][y-d1+i] = 5

    for i in range(d1):
        k = 1
        while (Arr_map[x+i+k][y-i]!=5):
            Arr_map[x+i+k][y-i] = 5
            k += 1
    for i in range(d2):
        k =1
        while (Arr_map[x+i+k][y+i] != 5):
            Arr_map[x+i+k][y+i] = 5
            k +=1

    for i in range(N):
        for j in range(N):
            if Arr_map[i][j] == 1:
                diff[0] += Arr_popul[i][j]
            elif Arr_map[i][j] == 2:
                diff[1] += Arr_popul[i][j]
            elif Arr_map[i][j] == 3:
                diff[2] += Arr_popul[i][j]
            elif Arr_map[i][j] == 4:
                diff[3] += Arr_popul[i][j]
            elif Arr_map[i][j] == 5:
                diff[4] += Arr_popul[i][j]
    diff.sort()
    return diff[4] - diff[0]

for i in range(N):
    for j in range(N):

        x ,y = i, j
        d1, d2 = 1,1

        # 모든 경우에 대해서 실행
        while (x+d1+d2 < N) and y - d1 >= 0 and y+d2 < N:
            while (x+d1+d2 < N) and y - d1 >= 0 and y+d2 < N:
                result = find_line(x,y,d1,d2)
                answer = min(answer, result)

                d2 += 1
            d2 = 1
            d1 += 1

print(answer)

