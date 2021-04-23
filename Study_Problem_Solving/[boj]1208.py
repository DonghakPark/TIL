"""
부분수열의 합 2 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

from sys import stdin
from collections import defaultdict


def dfs(idx, end_idx, subtotal, direction):
    global answer

    if idx == end_idx:
        if direction == "right":
            answer += left[s - subtotal]
        else:
            left[subtotal] += 1
        return

    dfs(idx + 1, end_idx, subtotal, direction)
    dfs(idx + 1, end_idx, subtotal + nums[idx], direction)


if __name__ == "__main__":
    answer = 0
    n, s = map(int, stdin.readline().split())
    nums = list(map(int, stdin.readline().split()))
    left = defaultdict(int)

    dfs(0, n//2, 0, "left")
    dfs(n//2, n, 0, "right")

    print(answer if s != 0 else answer - 1)