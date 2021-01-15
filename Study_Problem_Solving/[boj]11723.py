"""
집합 문제
author : donghak park
contact : donghark03@naver.com
"""
import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    com = input().split()

    if len(com) == 1:
        com0 = com[0]
    else:
        com0,com1 = com

    if com0 == "add":
        S.add(int(com1))

    elif com0 == "remove":
        if int(com1) in S:
            S.remove(int(com1))

    elif com0 == "check":
        if int(com1) in S:
            print(1)
        else:
            print(0)

    elif com0 == "toggle":
        if int(com1) in S:
            S.remove(int(com1))
        else:
            S.add(int(com1))

    elif com0 == "all":
        S = {1,2,3,4,5,6,7,8,9,10,
             11,12,13,14,15,16,17,18,19,20}

    else:
        S.clear()
