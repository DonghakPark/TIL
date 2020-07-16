T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.pop(0)
    arr.pop()
    print("#{} {}".format(test_case, round(sum(arr)/len(arr) ) ))