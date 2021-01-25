"""
트리의 순회 문제
author : donghak park
contact: donghark03@naver.com
TODO : 나중에 다시 풀어 볼 것
"""
import sys
sys.setrecursionlimit(10 ** 6)


def find_solution(l_in, r_in, l_post, r_post):

    if l_in > r_in or l_post > r_post:
        return

    parent = post_order[r_post]
    print(parent, end = " ")

    S_idx = idx[parent]
    left = S_idx - l_in

    find_solution(l_in, S_idx - 1, l_post, (l_post + left) - 1)
    find_solution(S_idx + 1, r_in, l_post + left, r_post - 1)


N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

idx = [0] * (N+1)
for i in range(N):
    idx[in_order[i]] = i

find_solution(0, N - 1, 0, N - 1)