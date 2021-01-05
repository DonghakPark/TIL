"""
못생긴 수 문제
author : donghak park
contact : donghark03@naver.com
"""
N = int(input())
result = [1,2,3,4,5]

if N <= 5:
    print(result[N-1])
else:
    temp = 6
    while len(result) < N:

        for element in result:
            if temp%element == 0:
                A = temp//element
                if A in result:
                    result.append(temp)
                    break
        temp += 1

    print(result[-1])