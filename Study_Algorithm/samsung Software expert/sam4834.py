T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = input()
    arr = list(map(int, arr))
    arr2 = [0] * (10)
    for i in range(N):
        arr2[arr[i]] += 1
    print(arr2)
    max_index, max_num = 0,0

    for i in range(0,10):
        if arr2[i] >= max_index:
            max_index = arr2[i]
            max_num = i

    print("#%d %d %d" %(test_case, max_num, max_index ))