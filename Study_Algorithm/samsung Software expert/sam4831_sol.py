T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    station_1st = [0] *(N+1)
    for i in range(len(station)):
        station_1st[station[i]] += 1

    start = 0
    end = K
    cnt = 0

    while True:
        zero = 0
        for i in range(start+1, end+1):
            if station_1st[i] == 1:
                start = i
            else:
                zero += 1

        if zero == K:
            cnt =0
            break

        cnt += 1
        end = start +K

        if end >= N:
            break
    print("#%d %d" %(test_case, cnt))
