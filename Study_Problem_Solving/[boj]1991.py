"""
트리 순회 문제
author : donghak park
contact: donhark03@naver.com
"""


def pre(current):
    if current == ".":
        return
    else:
        left,right = tree[current]
        print(current, end="")
        pre(left)
        pre(right)

def mid(current):
    if current == ".":
        return
    else:
        left, right = tree[current]
        mid(left)
        print(current, end="")
        mid(right)

def post(current):
    if current ==".":
        return
    else:
        left, right = tree[current]
        post(left)
        post(right)
        print(current, end = "")


N = int(input())

tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

pre("A")
print()
mid("A")
print()
post("A")
