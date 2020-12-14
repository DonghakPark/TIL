N = int(input())
arr_n = list(map(int, input().split()))

M = int(input())
arr_m = list(map(int, input().split()))

for element in arr_m:
    if element in arr_n:
        print('1')
    else:
        print('0')