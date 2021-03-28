T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    ans = 0
    for i in range(N):
        r_cnt = 0
        c_cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                r_cnt += 1
            elif r_cnt == K and arr[i][j] == 0:
                ans += 1
                r_cnt = 0
            else:
                r_cnt = 0

            if arr[j][i] == 1:
                c_cnt += 1
            elif c_cnt == K and arr[j][i] == 0:
                ans += 1
                c_cnt = 0
            else:
                c_cnt = 0
        if r_cnt == K:
            ans += 1
        if c_cnt == K:
            ans += 1

    print('#{} {}'.format(tc, ans))
