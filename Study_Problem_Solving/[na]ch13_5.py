"""
연산자 끼워넣기 문제
author : donghak park
contact : donghark03@naver.com
"""
from itertools import permutations

N = int(input())

arr = list(map(int,input().split()))

a,b,c,d = map(int, input().split())
# + - * /
def calculate(op1, op2, op3):
    if op3 == "+":
        return op1 + op2
    elif op3 == "-":
        return op1 - op2
    elif op3 == "*":
        return op1 * op2
    else:
        if op1 < 0 and op2 > 0:
            op1 = op1 * -1
            result = op1//op2
            return result * -1
        else:
            return op1//op2

arr2 = (['+'] * a) + (['-'] * b) + (['*'] * c) + (['/'] * d)
test = list(set(permutations(arr2, N-1)))

max_v = -2e9
min_v = 2e9

print(test)

while test:
    t = test.pop(0)

    first = arr[0]
    for i in range(1,N):
        first = calculate(first, arr[i], t[i-1])

    max_v = max(max_v, first)
    min_v = min(min_v, first)

print(max_v)
print(min_v)