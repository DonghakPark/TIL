"""
AC 문제
author : donghak park
contact : donghark03@naver.com
"""

T = int(input())
for test_case in range(T):
    C = input()
    N = int(input())
    arr = input().rstrip()[1:-1].split(",")

    if N == 0:
        arr = []

    l, r, re = 0, 0, True

    for com in C:
        if com == "R":
            re = not re
        else:
            if re is True:
                l += 1
            else:
                r += 1
    if r + l <= N:
        answer = arr[l:N - r]
        if re is True:
            print("[" + ",".join(answer) + "]")
        else:
            print("[" + ",".join(answer[::-1]) + "]")
    else:
        print("error")
