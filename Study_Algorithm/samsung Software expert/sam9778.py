T = int(input())
for i in range(1,T+1):
    N = int(input())
    arr = [4,4,4,4,4,4,4,4,16,4]
    card = list(map(int, input().split()))
    for element in card:
        arr[element-2] -= 1
    re = 21 - sum(card)
    under = sum(arr[0:(re-2)])
    over = sum(arr[(re-2):])
    if under <= over:
        print("STOP")
    else:
        print("GAZUA")

