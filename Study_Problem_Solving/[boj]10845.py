
import sys
input = sys.stdin.readline

N = int(input())
Arr = []
for i in range(N):

    S = input().split()

    if S[0] == "push" :
        Arr.append(S[1])
    elif S[0] == "pop":
        if len(Arr) == 0:
            print(-1)
        else:
            print(Arr.pop(0))
    elif S[0] == "size":
        print(len(Arr))
    elif S[0] == "empty":
        if len(Arr) == 0:
            print(1)
        else:
            print(0)
    elif S[0] == "front":
        if len(Arr) == 0 :
            print(-1)
        else:
            print(Arr[0])
    else:
        if len(Arr) == 0:
            print(-1)
        else:
            print(Arr[-1])
