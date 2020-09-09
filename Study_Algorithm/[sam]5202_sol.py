T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr1 = []
    for ser in range(N):
        a,b = map(int, input().split())
        arr1.append([a,b])
    arr1.sort(key=lambda x: (x[0], x[1]), reverse = True)

    ans, end = 0,0
    for m in arr1:
        if end <= m[0]:
            end = m[0]
            ans += 1
    print("#{} {}".format(test_case, ans))