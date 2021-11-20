"""
마법사 상어와 파이어스톰
Author : DongHak Park
"""
import copy

def rotate(sub_row):
    global ice
    temp = copy.deepcopy(ice)

    for i in range(0, row, sub_row):
        for j in range(0, row, sub_row):

            for c in range(j, j+sub_row):
                for r in range(i+sub_row-1, i, -1):
                    ice[c][j + sub_row-(r + 1)] = temp[r][c]

    for element in ice:
        print(element)

def remove():
    pass

def solution():
    pass

N,Q = map(int, input().split())
row = 2 ** N
ice = []
for _ in range(row):
    ice.append(list(map(int, input().split())))
L = list(map(int, input().split()))

for l in range(len(L)):
    sub_row = (2 ** L[l])

    rotate(sub_row)
    remove()

solution()