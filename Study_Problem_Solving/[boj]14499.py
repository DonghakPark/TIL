"""
주사위 굴리기 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

N, M, x, y, k = map(int, input().split())
dice_map = []

for _ in range(N):
    dice_map.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

