# 연산자 끼워 넣기
from itertools import permutations
from _collections import deque
import copy
import sys

def solve(n, num_list, operation_count_list):
    op = ['+','-','*','//']
    operation_list = []
    max = -sys.maxsize -1
    min = sys.maxsize

    for i in range(4):
        operation = op[i]
        count = operation_count_list[i]
        temp = [operation] * count
        operation_list.extend(temp)

    case_list = set(permutations(operation_list, n-1))

    for case in case_list:
        temp_list = deque(copy.deepcopy(num_list))
        idx = -1
        result = temp_list.popleft()
        while temp_list:
            idx += 1
            next_num = temp_list.popleft()
            current_op = case[idx]

            if current_op == '+':
                result += next_num
            elif current_op == '-':
                result -= next_num
            elif current_op =='*':
                result *=next_num
            else:
                if result < 0:
                    result = -(result)
                    result //= next_num
                    result = -(result)
                else:
                    result //= next_num
        if result < min:
            min = result

        if max < result:
            max = result

    return max, min

N = int(input())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

max, min = solve(N,A,C)
print(max)
print(min)