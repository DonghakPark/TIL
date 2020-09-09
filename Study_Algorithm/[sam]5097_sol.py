T= int(input())
for i in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for it in range(1, M+1):
        temp = arr.pop(0)
        arr.append(temp)
    print("#{} {}".format(i, arr[0]))