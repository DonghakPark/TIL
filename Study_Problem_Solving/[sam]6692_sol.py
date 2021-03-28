T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    avg = 0
    for i in range(1, N+1):
        p, x = map(float, input().split())
        avg += p*x
    print("#{} {}".format(test_case, avg))
