from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
Arr = deque()

for i in range(N):
    S = input().split()

    if S[0] == "push_front":
        Arr.appendleft(S[1])
    elif S[0] == "push_back":
        Arr.append(S[1])
    elif S[0] == "pop_front":
        if len(Arr) != 0:
            print(Arr.popleft())
        else:
            print(-1)
    elif S[0] == "pop_back":
        if len(Arr) != 0:
            print(Arr.pop())
        else:
            print(-1)
    elif S[0] == "size":
        print(len(Arr))
    elif S[0] == "empty":
        if len(Arr) == 0 :
            print(1)
        else:
            print(0)
    elif S[0] == "front":
        if len(Arr) != 0:
            print(Arr[0])
        else:
            print(-1)
    else:
        if len(Arr) != 0:
            print(Arr[-1])
        else:
            print(-1)