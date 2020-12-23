"""
안테나 문제
author : donghak park
contact : donghark03@naver.com
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

print(arr[(N-1)//2])