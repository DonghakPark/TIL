T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print("#%d %d" %(test_case, max(arr)-min(arr)))

