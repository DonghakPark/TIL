#벌꿀 채취 문제

T = int(input())


def find(arr, M, C):
    limit = C
    arr.sort(reverse=True)

    if sum(arr) > limit:

        while t:
            t = arr.pop(0)
            if t <= limit:
                limit -= t
                arr.append(t)
            else:
                continue
    m = 0
    for element in arr:
        m += element ** 2

    return m

for test_case in range(1, T+1):
    N, M, C = map(int, input().split())

    array = []
    for i in range(N):
        array.append(list(map(int,input().split())))
    ## 입력 완료

    result = []

    for i in range(N):
        for j in range(N):

            x,y = i, j
            if y + M > N and x != N-1:
                x2, y2 = i+1, j

            elif x == N-1:
                if y + M >N:
                    continue
                else:
                    x2, y2 = i, j+M
            else:
                x2, y2 = i, j+M

            temp1 = []
            temp2 = []


