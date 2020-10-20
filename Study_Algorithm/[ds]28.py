
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

N, M, K = map(int, input().split())

uni_map = [[[] for _ in range(N)] for _ in range(N)]
pla = []
for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    pla.append([r-1,c-1,m,s,d])

def move():
    global pla
    global uni_map

    while pla:
        x,y,m,s,d = pla.pop(0)
        nx = ( x + ( dx[d] * s ) ) % N
        ny = ( y + ( dy[d] * s ) ) % N

        uni_map[nx][ny].append([m,s,d])

def crush():

    for i in range(N):
        for j in range(N):

            if len(uni_map[i][j]) == 0:
                continue
            elif len(uni_map[i][j]) == 1:
                m,s,d = uni_map[i][j][0]
                pla.append([i,j,m,s,d])
                uni_map[i][j].clear()
            #행성이 두개 이상 있는 경우
            else:
                temp_s = 0
                temp_m = 0
                odd = 0
                even = 0
                for element in uni_map[i][j]:
                    m,s,d = element[0],element[1],element[2]
                    temp_m += m
                    temp_s += s

                    if d%2 == 0:
                        even +=1
                    else:
                        odd += 1
                start = 0
                if even == 0 or odd == 0:
                    start = 0
                else:
                    start = 1

                if int(temp_m/5) != 0:
                    for k in range(4):
                        pla.append([i,j,int(temp_m/5),  int(temp_s/len(uni_map[i][j])),start + (k*2)] )

                uni_map[i][j].clear()

def get_answer():
    answer = 0

    for element in pla:
        answer += element[2]

    return answer

time = 1

while time <= K:
    move()
    # print("move:",pla,"--",uni_map)
    crush()
    # print("crush:",pla,'--',uni_map)
    time += 1

print(get_answer())